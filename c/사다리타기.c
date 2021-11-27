#include <stdio.h>
#include <stdlib.h> // rand() 함수 포함 라이브러리

int* get_cases(int coulumn);

int main() {
    int numArr[8][4] = {
        {0,0,0,0},
        {0,0,0,1},
        {0,0,1,0},
        {0,1,0,0},
        {0,1,0,1},
        {1,0,0,0},
        {1,0,0,1},
        {1,0,1,0}
    };
    
    int num = 7; // 사람수
    int coulumn = num - 1; // 가로
    int row = 10; // 세로 (사다리가 얼마나 긴가)
    //int arr[row][coulumn]; 
    //int* arr[row] = (int*)malloc(coulumn)
    int **arr;
    arr = (int**) malloc ( sizeof(int*) * row );
    
    int winner = 3; // 당첨번호 5번
    // 사다리 1등 데이터 초기화
    int result[num] ;//= {0,};
    for(int i=0; i<num; i++) {
        result[i] = 0;
    }

    // 50번 실행
    for(int t=0; t<50; t++) {
        //get_cases(4);
        printf("\n");
        for(int i=0; i<row; i++) {
            arr[i] = get_cases(coulumn);
            for(int j=0; j<coulumn; j++) {
                printf("%d", arr[i][j]);
            }
            printf("\n");
        }
        
        printf("계산 시작\n");
        
        int index = winner;
        for(int j=0; j<row; j++) {
            for(int j=0; j<coulumn; j++) {
                if (index < coulumn && *arr[index+1]==1) {
                    index = index +1;
                }
                else if(index > 0 && *arr[index-1]==1) {
                    index = index -1;
                }
            }
        }
        result[index] = result[index]+1;
        
        // 해제
        for(int i=0; i<row; i++){
            free(arr[i]);
        }
    }

    // 결과 출력
    for(int i=0; i<num; i++) {
        printf("%d ", result[i]);
    }
    
   
    return 0;
}

// 조건문을 이용하면 단점이 많고 재귀방식은 너무 복잡함
// 1연속 두번일 경우 예외처리
int* get_cases(int coulumn) {
    int *arr = (int*)malloc(coulumn); 
    for (int i = 0; i<coulumn; i++) {
        arr[i] = rand()%2;
    }
    return arr;
}
