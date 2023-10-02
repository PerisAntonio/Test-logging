import logging

def run(input_data, solver_params, extra_arguments):
    logging.basicConfig(level=logging.DEBUG,filename='solver.log',filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')
    logging.warning('This is a warning')
    logging.debug('This is a debug')
    ret={}
    ret['Output']='Success'
    return ret
    