class integer_to_roman{
	public String intToRoman(int num){
		final int[] INTEGERS = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
		final String[] ROMANS = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
		
		for(int i = 0; i < INTEGERS.length; i++){
			if (num>=INTEGERS[i]){
				return ROMANS[i] + intToRoman(num - INTEGERS[i]);
			}	
		}
		return "";
	}
}


//class Main{
//	public static void main(String []args){
//		integer_to_roman sol = new integer_to_roman();
//		System.out.println(sol.intToRoman(3));
//	}
//}




