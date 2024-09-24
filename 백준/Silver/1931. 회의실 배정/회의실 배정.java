import javax.swing.text.html.parser.Entity;
import java.io.*;
import java.util.*;

public class Main {
    static class Time {
        int start;
        int end;

        public Time(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());

        List<Time> times = new ArrayList<>();

        for(int i=0; i<t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            times.add(new Time(start, end));
        }

        times.sort((t1, t2) -> {
            if (t1.end == t2.end) {
                return Integer.compare(t1.start, t2.start);
            }
            return Integer.compare(t1.end, t2.end);
        });

        int count = 0;
        int endTime = 0;

        for (Time time : times) {

            if(time.start >= endTime) {
                endTime = time.end;
                count++;
            }
        }

        bw.write(count+"\n");
        bw.flush();
    }
}