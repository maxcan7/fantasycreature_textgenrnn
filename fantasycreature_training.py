#!/usr/bin/env py
import pandas as pd
import fantasycreature_pretrain_config as cfg
from textgenrnn import textgenrnn
import os
import shutil

mainpath = cfg.pretrain_cfg['mainpath']
datapath = cfg.pretrain_cfg['datapath']
modelname = cfg.pretrain_cfg['modelname']


def load_data(datapath=datapath):
    df = pd.read_csv(datapath)
    return df


def preprocess_data(df):
    fantasycreature = df['Name'].str.replace('(-[a-z0-9]+)', '').str.capitalize().unique().tolist()
    return fantasycreature


def run_model(modelname, fantasycreature):
    textgen = textgenrnn(name=modelname)
    textgen.train_on_texts(fantasycreature, max_length=4, num_epochs=100, gen_epochs=20, new_model=True, rnn_size=16, rnn_layers=4, dropout=0.5)


def move_configs(modelname):
    shutil.move(mainpath + modelname + '_config.json', mainpath + 'config/' + modelname + '_config.json')
    shutil.move(mainpath + modelname + '_vocab.json', mainpath + 'config/' + modelname + '_vocab.json')
    shutil.move(mainpath + modelname + '_weights.hdf5', mainpath + 'config/' + modelname + '_weights.hdf5')


if __name__ == '__main__':
    df = load_data()
    fantasycreature = preprocess_data(df)
    run_model(modelname, fantasycreature)
    move_configs(modelname)
