#include <stdio.h>

int main() {
    int num = 2;
    int day = 7;
    int time[num][day];
    for(int i=0; i<num; i++) {
        printf("학생 %d의 공부 시간을 입력하세요\n", i+1);
        for(int j=0; j<day; j++) {
            scanf("%d", &time[i][j]);
        }
    }

    printf("계산 시작\n");
    int max = 0;
    for(int i=0; i<num; i++) {
        int compare = 0;
        for(int j=0; j<day; j++) {
            
        }
    }
    return 0;
}
  
