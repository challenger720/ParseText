awk '{
  print "Line: " NR;
  print "Name: " $1;
  print "Points: " $2;
  print "===";
  print "";
}' file.txt
