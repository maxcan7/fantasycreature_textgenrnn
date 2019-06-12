#!/usr/bin/env py
from textgenrnn import textgenrnn
import fantasycreature_generate_config as cfg

weights = cfg.gen_cfg['weights']
vocab = cfg.gen_cfg['vocab']
config = cfg.gen_cfg['config']
modelname = cfg.gen_cfg['modelname']


def fantasycreature_generate(weights, vocab, config, modelname):
    textgen = textgenrnn(weights_path=weights,
                         vocab_path=vocab,
                         config_path=config)
    textgen.generate_to_file(modelname + '_gen.txt', n=500, temperature=[1.0, 0.5, 0.5])


if __name__ == '__main__':
    fantasycreature_generate(weights, vocab, config, modelname)
