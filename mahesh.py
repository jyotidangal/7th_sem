meroArray=[1,4,5,6,0]
console.log(`the given array is meroArray[]=${meroArray}`)
let n =meroArray.length

for(let i=1; i<n; i++)
{   
    console.log(`for i = ${i}`)
    let current = meroArray[i];
    console.log(`current = meroArray[${i}] = (${meroArray[i]})`)
    let j =i-1
    console.log(`j = i-1 = ${j}`)
    while(meroArray[j]>current)
    {
        console.log(` since, meroArray[${j}]> current (i.e ${current})`)
        meroArray[j+1]=meroArray[j]
        console.log(`meroArray[j+1] (meroArray[${j+1}])=meroArray[j] ${meroArray[j]}`)
        j--;
    }
    
    meroArray[j+1]=current;
}
for(let i=0; i<n; i++)
{
    console.log(meroArray[i])
    console.log()
}
