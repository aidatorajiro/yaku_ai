FILE=$1

echo "Note: available models are horse2zebra, zebra2horse"

echo "Specified [$FILE]"

mkdir -p ./checkpoints/${FILE}_pretrained
MODEL_FILE=./checkpoints/${FILE}_pretrained/latest_net_G.pth
URL=https://people.eecs.berkeley.edu/~taesung_park/pytorch-CycleGAN-and-pix2pix/models/$FILE.pth

curl $URL -o $MODEL_FILE


