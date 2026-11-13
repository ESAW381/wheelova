// Wheelova probability simulation: replicates the spin math in https://wheelova.com/app.js
// (same as /data/fairness/wheelova-spin-test.js) and measures, for a wheel with n entries:
//  - how many spins it takes until every entry has won at least once (Remove winner OFF)
//  - how many entries are never picked in n spins (Remove winner OFF)
// Run with Node 18+: node wheelova-probability-sim.js
const {webcrypto}=require('crypto');const TAU=Math.PI*2;
function rand(){const a=new Uint32Array(1);webcrypto.getRandomValues(a);return a[0]/4294967296}
function idxAt(r,n){const seg=TAU/n;const a=((-r)%TAU+TAU)%TAU;return Math.min(n-1,Math.floor(a/seg))}
function trial(n){let rot=0,seen=new Set(),spins=0,missedAtN=0;
 while(seen.size<n){const target=rot+TAU*6+rand()*TAU;rot=target%TAU;seen.add(idxAt(rot,n));spins++;if(spins===n)missedAtN=n-seen.size}
 if(spins<n)missedAtN=0;return [spins,missedAtN]}
const RUNS=100000,out={};
for(const n of [6,10,25]){const t=[];let miss=0;for(let i=0;i<RUNS;i++){const [s,m]=trial(n);t.push(s);miss+=m}
 t.sort((a,b)=>a-b);out[n]={runs:RUNS,mean:+(t.reduce((a,b)=>a+b,0)/RUNS).toFixed(2),median:t[RUNS/2],p90:t[Math.floor(RUNS*0.9)],min:t[0],max:t[RUNS-1],avgNeverPickedInNSpins:+(miss/RUNS).toFixed(2)}}
console.log(JSON.stringify(out,null,1));
