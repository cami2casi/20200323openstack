#!/usr/bin/python3

# accept commands form cli
import argparse

import json

def main():
    inventory = {}
    if args.list:
        inventory = example_inventory()
    elif args.host:
        inventory = empty_inventory()
    else:
        inventory = empty_inventory()

    print(json.dumps(inventory))


def example_inventory():
    return {
        'group': {
            'hosts': ['centurylink-webserver']
            },
        '_meta': {
            'hostvars': {
                'centurylink-webserver': {
                    'ansible_connection': 'local',
                    'ansible_host': 'localhost'
                        }
                    }
                }
            }

def empty_inventory():
    return {}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', action = 'store_true')
    parser.add_argument('--host', action = 'store')
    args = parser.parse_args()
    main()
  


