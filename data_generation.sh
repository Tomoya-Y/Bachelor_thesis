cd data_extraction 
#bash automan_based_bash.sh $1 ../$3
bash automan_based_bash.sh $1 $2
python3 moving_average.py $2
#cd ../data_argmentation
#bash maker.sh $3 $2
#rm -rf output_tmp
