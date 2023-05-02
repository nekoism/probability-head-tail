public class MyClass {
    public static void main(String args[]) {
        int heads = 0;
        int tails = 0;
        int n = 100000000; // number of trials 
        int random = (int)(Math.random() * 1 + 1);
        for(int i = 0; i < n; i++){
            random = (int)(Math.random() * 2);
            if(random == 0){
                heads++;
            }else if(random == 1){
                tails++;
            }
        }
        System.out.println("After flipping " + n + " coins we got heads: " + heads + " and prob of getting heads " + (((float)heads/n)*100) + "% coins we got tails: " + tails + " and prob of getting tails " + ((float)tails/n*100) + "%" );
        
    }
}
