funksiya bubblesort[
dəyişən ok=0
dövr ok=>(ok<uzunluq(sirasi)){
dəyişən j=0
dövr j=>(j<(uzunluq(sirasi)-ok-1)){
əgər sirasi[j]>sirasi[j+1]:dəyişən müvəq=sirasi[j];dəyişən sirasi[j]=sirasi[j+1];dəyişən sirasi[j+1]=müvəq
dəyişən j=j+1
}j
dəyişən ok=ok+1
}ok
yaz sirasi
]bubblesort
dəyişən sirasi=[9, 4, 2, 3, 8, 7, 10, 1, 6, 5]
çağır bubblesort
