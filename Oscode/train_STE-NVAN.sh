CKPT=ckpt_STENVAN_0230_20191202
TRAIN_INFO=/home/amurtiger/WJHscripts/tiger_MARS_database20191202/train_info.npy
TEST_INFO=/home/amurtiger/WJHscripts/tiger_MARS_database20191202/test_info.npy
TRAIN_TXT=/home/amurtiger/WJHscripts/tiger_MARS_database20191202/train_path.txt
TEST_TXT=/home/amurtiger/WJHscripts/tiger_MARS_database20191202/test_path.txt
QUERY_INFO=/home/amurtiger/WJHscripts/tiger_MARS_database20191202/query_IDX.npy

python3 train_NL.py --train_txt $TRAIN_TXT --train_info $TRAIN_INFO  --batch_size 32 \
                    --test_txt $TEST_TXT  --test_info  $TEST_INFO   --query_info $QUERY_INFO \
                    --n_epochs 200 --lr 0.0001 --lr_step_size 50 --optimizer adam --ckpt $CKPT --log_path loss.txt --class_per_batch 8 \
                    --model_type 'resnet50_NL_stripe_hr' --num_workers 8 --track_per_class 4 --S 8 --latent_dim 2048 --temporal Done  --track_id_loss \
                    --non_layers  0 2 3 0 --stripes 16 16 16 16 