for file in `\find /media/tomoya/Tomoya\'s_T5/Masterbag/ -name '*.bag'`; do
  IFS='/.'
  set -- $file
  input="/media/tomoya/Tomoya's_T5/Masterbag/${6}.bag"
  input2="/media/tomoya/Tomoya's_T5/sotsuron_data/output${6}"
  output="../../output_tmp${6}"
  rmout="../../output_tmp${6}"
  echo "$input"
  echo "$input2"
  #mkdir ${output}
  bash data_generation.sh "$input" "$input2" "$output"
  #rm -rf "$rmout"
done
	
