import java.util.Scanner;

class App {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int arr[] = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = in.nextInt();
        }
        int j = 1, cnt = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == j) {
                j++;

            } else {
                System.out.println(j);
                j++;
                cnt++;
            }
        }
        if (cnt == 0) {
            System.out.println("good job");
        }
    }
}