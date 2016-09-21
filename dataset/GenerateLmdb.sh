# Extract ILSVRC2013_DET_val.tar to ILSVRC2013_DET_val
# Extract ILSVRC2014_DET_train to ILSVRC2014_DET_train, and extract all nXXXXXXXX.tar files in this folder

python ILSVRC2013_DET_val.py
python ILSVRC2014_DET_train.py

convert_imageset --resize_width 128 --resize_height 128 --shuffle ILSVRC2014_DET_train/ ILSVRC2014_DET_train.txt ILSVRC2014_DET_train_lmdb
convert_imageset --resize_width 128 --resize_height 128 --shuffle ILSVRC2013_DET_val/ ILSVRC2013_DET_val.txt ILSVRC2013_DET_val_lmdb_class1

compute_image_mean ILSVRC2014_DET_train_lmdb ILSVRC2014_DET_train_lmdb/mean.binaryproto
