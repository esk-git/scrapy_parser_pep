import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.status_sum = defaultdict(int)

    def process_item(self, item, spider):
        self.status_sum[item['status']] += 1
        return item

    def close_spider(self, spider):
        time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        path = BASE_DIR / f'results/status_summary_{time}.csv'
        with open(path, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(['Статус', 'Количество'])
            total = sum(self.status_sum.values())
            writer.writerows(self.status_sum.items())
            writer.writerow(['Total', total])
