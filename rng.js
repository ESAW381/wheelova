/* Wheelova random helpers. Uses crypto.getRandomValues; integers are drawn by
   rejection sampling, so every outcome in [0, n) is exactly equally likely. */
(function(root){
var TWO32=4294967296,TWO53=9007199254740992;
var R={
 u32:function(){var a=new Uint32Array(1);root.crypto.getRandomValues(a);return a[0]},
 // float in [0,1) for continuous uses (wheel angle)
 rand:function(){return R.u32()/TWO32},
 // uniform integer in [0, n), n integer with 1 <= n <= 2^53
 randInt:function(n){
  if(!(n>=1&&n<=TWO53&&Math.floor(n)===n))throw new RangeError('randInt: n must be an integer from 1 to 2^53');
  if(n===1)return 0;
  if(n<=TWO32){var lim=TWO32-(TWO32%n),u;do{u=R.u32()}while(u>=lim);return u%n}
  var lim2=TWO53-(TWO53%n),x;do{x=(R.u32()>>>11)*TWO32+R.u32()}while(x>=lim2);return x%n},
 shuffle:function(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=R.randInt(i+1),t=a[i];a[i]=a[j];a[j]=t}return a}
};
root.WVRNG=R;if(typeof module!=='undefined'&&module.exports)module.exports=R;
})(typeof window!=='undefined'?window:globalThis);
