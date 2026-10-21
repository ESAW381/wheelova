// Wheelova fairness test: replicates the spin math in https://wheelova.com/app.js
// Run with Node 18+: node wheelova-spin-test.js
// Replicates Wheelova's spin math from app.js exactly.
const {webcrypto}=require('crypto');const TAU=Math.PI*2;
function rand(){const a=new Uint32Array(1);webcrypto.getRandomValues(a);return a[0]/4294967296}
function idxAt(r,n){const seg=TAU/n;const a=((-r)%TAU+TAU)%TAU;return Math.min(n-1,Math.floor(a/seg))}
function run(n,spins,turns){let rot=0;const out=new Uint8Array(spins);
 for(let s=0;s<spins;s++){const target=rot+TAU*turns+rand()*TAU;rot=target%TAU;out[s]=idxAt(rot,n)}return out}
const fs=require('fs');
// Writes one digit per spin (0 = first entry) for the 10-entry and 2-entry wheels.
for(const [n,label] of [[10,'ten'],[2,'two'],[6,'six']]){const r=run(n,1000000,6);fs.writeFileSync(label+'-entries-1m-spins.txt',Array.from(r).join(''))}
console.log('done')
