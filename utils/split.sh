echo "Processing 1"
sed -n '2,9997146p' security_train.csv  >> split_1.csv
echo "Processing 2"
sed -n '9997147,19976785p' security_train.csv  >> split_2.csv
echo "Processing 3"
sed -n '19976786,29999848p' security_train.csv  >> split_3.csv
echo "Processing 4"
sed -n '29999849,40004253p' security_train.csv  >> split_4.csv
echo "Processing 5"
sed -n '40004254,49946336p' security_train.csv  >> split_5.csv
echo "Processing 6"
sed -n '49946337,59995003p' security_train.csv  >> split_6.csv
echo "Processing 7"
sed -n '59995004,70005628p' security_train.csv  >> split_7.csv
echo "Processing 8"
sed -n '70005629,80000231p' security_train.csv  >> split_8.csv
echo "Processing 9"
sed -n '80000232,89806694p' security_train.csv  >> split_9.csv
