import os
import json
import xml.etree.ElementTree as ET


def read_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def result2txt(json_result_file, out_result_path):
    if not os.path.exists(out_result_path):
        os.makedirs(out_result_path)
    result_info_list = read_json(json_result_file)
    for result_info in result_info_list:
        file_name = result_info['filename']
        box_info_list = result_info['output']
        file_name_txt = file_name[:-4] + '.txt'
        file_path_txt = os.path.join(out_result_path, file_name_txt)
        with open(file_path_txt, 'w', encoding='utf-8') as f:
            for box_info in box_info_list:
                f.write(box_info['comment'] + ' ' + str(box_info['score']) + ' ' + str(box_info['x1']) + ' ' +
                        str(box_info['y1']) + ' ' + str(box_info['x2']) + ' ' + str(box_info['y2']) + '\n')


def voc2txt(xml_path, out_path):
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    for file_name in os.listdir(xml_path):
        xml_file_path = os.path.join(xml_path, file_name)
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
        objects = root.findall('object')
        out_txt_file = os.path.join(out_path, file_name[:-3] + 'txt')
        with open(out_txt_file, 'w', encoding='utf-8') as f:
            for _object in objects:
                label = _object.find('name').text
                xml_bndbox = _object.find('bndbox')
                xmin = xml_bndbox.find('xmin').text
                ymin = xml_bndbox.find('ymin').text
                xmax = xml_bndbox.find('xmax').text
                ymax = xml_bndbox.find('ymax').text
                f.write(label + ' ' + xmin + ' ' + ymin + ' ' + xmax + ' ' + ymax + '\n')


if __name__ == '__main__':
    json_result_file = r'D:\result\merge_0601\result_test_7500_22_dino_5scale_swin_l_8xb2_50e_50_8850'
    out_result_path = r'D:\result\merge_0601\txt_result_test_7500_22_dino_5scale_swin_l_8xb2_50e_50_8850'
    result2txt(json_result_file, out_result_path)

    # json_result_file = r'D:\result\nr_train1_23\result_val_nr_train1_23_yolov7_best_288_7774_17'
    # out_result_path = r'D:\result\nr_train1_23\txt_result_val_nr_train1_23_yolov7_best_288_7774_17'
    # result2txt(json_result_file, out_result_path)

    # xml_path = r'D:\data\test\nr_val\val\xml_17'
    # out_path = r'D:\data\test\nr_val\val\txt_17'
    # voc2txt(xml_path, out_path)