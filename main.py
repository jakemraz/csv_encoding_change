import sys
import csv



def convert(input, output, in_encoding, out_encoding):
  print('start convert')

  input_f = open(input, 'r', encoding=in_encoding)
  output_f = open(output, 'w', encoding=out_encoding)
  input_csv = csv.reader(input_f)
  output_csv = csv.writer(output_f)


  

  for line in input_csv:
    print(line)
    output_csv.writerow(line)

  
  input_f.close()
  output_f.close()


if len(sys.argv) == 1:
  print('### how to use ###')
  print('python3 main.py $INPUTFILE $OUTPUTFILE $INPUT_ENCODING $OUTPUT_ENCODING')
  print('')
  print('### Example ###')
  print('python3 main.py input.csv output.csv utf-8-sig utf-8')
elif len(sys.argv) == 5:
  convert(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
else:
  print('read how to use again')




