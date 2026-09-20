def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

print is_int(10)
print is_int(10.5)

#with this function you can make number with float like 7.0 as the same behaviour like the integer 7. The other float number will be false if we introde them in the function
