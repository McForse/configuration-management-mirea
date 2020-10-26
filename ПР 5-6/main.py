import json

data = ''' json '''
json_str = json.loads(data)


if __name__ == '__main__':
    cleanList = []
    for item in json_str:
        print('{}: {}'.format(item, ' '.join(json_str[item])))
        print('\t@echo "{}" > {}'.format(item, item))
        cleanList.append(item)
    print('.PHONY = clean\nclean:\n\t@rm {}\n\t@echo "Files deleted"'.format(' '.join(cleanList)))
