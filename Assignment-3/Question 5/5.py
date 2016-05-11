from __future__ import division
import json
import math

import sys

def ratio():
    merged_file_path = '../size_ratio.json'
    temp_ratio = open('final_ratio.json', 'w+')
    i = 0
    max_ratio = {}
    with open(merged_file_path) as lines:
        for line in lines:
            i += 1
            solr_index_size = sys.getsizeof(line)
            json_line = json.loads(line.strip())
            content_type = json_line['Content-Type']
            content_type = content_type.split(';')[0]
            new_json = {'id': json_line['id'], 'Content-Type': content_type}
            file_size = json_line['file_size']
            ratio = solr_index_size / file_size
            if content_type in max_ratio:
                if ratio > max_ratio[content_type]:
                    max_ratio[content_type] = ratio
            else:
                max_ratio[content_type] = ratio
            new_json['ratio'] = ratio
            json.dump(new_json, temp_ratio)
            temp_ratio.write('\n')
    return max_ratio


def normalize(max_ratio):
    temp_ratio = 'temp_ratio.json'
    ratio_file = open('ratio.json', 'w+')
    i = 0
    with open(temp_ratio) as lines:
        for line in lines:
            i += 1
            json_line = json.loads(line.strip())
            content_type = json_line['Content-Type']
            new_json = {'id': json_line['id'], 'Content-Type': content_type}
            ratio = json_line['ratio']
            ratio = ratio / max_ratio[content_type]
            ratio = math.sqrt(ratio)
            new_json['ratio'] = ratio
            json.dump(new_json, ratio_file)
            ratio_file.write('\n')

ratio()