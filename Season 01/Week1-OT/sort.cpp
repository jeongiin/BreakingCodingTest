#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void swap(vector<int>& list, int a, int b) {
    int temp = list[a];
    list[a] = list[b];
    list[b] = temp;
}

void printVector(vector<int>& v) {
    for (auto e : v) {
        cout << e << "\t";
    }
    cout << endl << endl;
}

void bubbleSort(vector<int>& list) {
    int i, j;
    int n = list.size();

    // i : Ž���� ���� --> (n-1) ~ 0 ���� �ݺ�
    // j : �ϳ��� ���ϱ����� index 

    for (i = n - 1; i > 0; i--) {
        for (j = 0; j < i; j++) {
            // j��°�� j+1��°�� ��Ұ� ũ�� ���� �ƴϸ� ��ȯ
            if (!(list[j] <= list[j + 1])) {
                swap(list, j, j + 1);
            }
        }
    }
}

int getMinIndex(vector<int>& list, int start) {
    int minIndex = start;
    int minValue = 10001;

    for (int j = start; j < list.size(); j++) {
        if (minValue > list[j]) {
            minIndex = j;
            minValue = list[j];
        }
    }

    return minIndex;
}

void selectionSort(vector<int>& list) {

    int n = list.size();

    for (int i = 0; i < n - 1; i++) {
        // i ~ n-1 ���ұ��� �ּڰ��� idx Select
        int minIndex = getMinIndex(list, i);

        // i�� �ּڰ� idx ����
        if (i != minIndex) {
            swap(list, i, minIndex);
        }
    }
}

bool cmp(int left, int right) {
    return left > right;
}