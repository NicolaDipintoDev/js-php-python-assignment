// I believe that clean code doesn't need comments excpet for very complicated algorithms

const reverse_binary = number => {
  const decimalToBinary = number => number.toString(2);
  const reverse = string => string.split("").reverse().join("");
  const binaryToDecimal = number => (parseInt(number, 2));
  console.log(binaryToDecimal(reverse(decimalToBinary(number))));
}

reverse_binary(13);