from elasticsearch import Elasticsearch

def create_client(config):
    """
    Sends a request with the credentials to interact with elasticsearch
    Arguments - 
    config : python file with the parameters 
    """
    global client
    client = Elasticsearch(config['es_config']['es_url'], scheme='http', port=config['es_config']['es_port'], sniff_on_start=True, sniff_on_connection_fail=True, sniffer_timeout=6000, timeout=1200, max_retries=10, retry_on_timeout=True)


def get_client():
    """
    Returns client created to interact with elasticsearch
    """
    return client
