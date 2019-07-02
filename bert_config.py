#encoding=utf-8
class BertConfig(object):
    def __init__(self):
        #数据地址
        self.data_dir='bert_data'
        self.bert_config_file='chinese_L-12_H-768_A-12/bert_config.json'
        self.task_name='mycla'
        self.vocab_file='chinese_L-12_H-768_A-12/vocab.txt'
        self.output_dir='bert_output'
        self.init_checkpoint='chinese_L-12_H-768_A-12/bert_model.ckpt'
        self.max_seq_length=128
        self.do_train=True
        self.do_eval=True
        self.do_predict=False
        self.train_batch_size=32
        self.eval_batch_size=8
        self.predict_batch_size=8
        self.learning_rate=5e-5
        self.num_train_epochs=2
        self.save_checkpoints_steps=1000
        self.use_gpu='0'