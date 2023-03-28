def process(**args):
    for arg in args:
        print(arg , ' -->> ', args[arg])
    print('args = ', args)

process(name='iNightjar', job ='Software Engineer', age=23, mentality= 'Winner', Leader = True)



