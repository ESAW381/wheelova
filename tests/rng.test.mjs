// Run: node --test tests/   (no dependencies)
import test from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const R = require('../rng.js');
const real = R.u32;
function feed(values){ let i = 0; R.u32 = () => { if (i >= values.length) throw new Error('out of mocked values'); return values[i++]; }; }
test.afterEach(() => { R.u32 = real; });

test('rejects invalid n', () => {
  for (const n of [0, -1, 1.5, NaN, 2 ** 53 + 2, Infinity]) assert.throws(() => R.randInt(n), RangeError);
});
test('n = 1 always 0 and consumes no randomness', () => { feed([]); assert.equal(R.randInt(1), 0); });
test('n = 6: values below the limit map by modulo', () => { feed([0, 5, 6, 4294967291]); assert.deepEqual([R.randInt(6), R.randInt(6), R.randInt(6), R.randInt(6)], [0, 5, 0, 5]); });
test('n = 6: values at/above the rejection limit are redrawn', () => {
  const lim = 4294967296 - (4294967296 % 6); // 4294967292
  feed([lim, 4294967295, 7]); assert.equal(R.randInt(6), 1);
});
test('n = 3: limit and rejection', () => { const lim = 4294967296 - (4294967296 % 3); feed([lim, lim - 1]); assert.equal(R.randInt(3), (lim - 1) % 3); });
test('n = 2^32 never rejects', () => { feed([4294967295]); assert.equal(R.randInt(2 ** 32), 4294967295); });
test('n > 2^32 uses 53 bits', () => {
  // hi word >>> 11 gives 21 bits; x = hi21 * 2^32 + lo
  feed([0xFFFFFFFF, 0xFFFFFFFF]); const n = 2 ** 53 - 1; const x = (0xFFFFFFFF >>> 11) * 2 ** 32 + 0xFFFFFFFF; // 2^53 - 1
  const lim = 2 ** 53 - (2 ** 53 % n); assert.ok(x >= lim); // must be rejected
  feed([0xFFFFFFFF, 0xFFFFFFFF, 0, 123]); assert.equal(R.randInt(n), 123);
});
test('large range: every residue mod 1000 is reachable for 1..1e12', () => {
  const seen = new Set(); for (let i = 0; i < 20000 && seen.size < 1000; i++) seen.add(R.randInt(1e12) % 1000);
  assert.equal(seen.size, 1000);
});
test('outputs always in range', () => {
  for (const n of [2, 3, 7, 10, 1000, 2 ** 31 + 1, 2 ** 33 + 7, 2 ** 53]) for (let i = 0; i < 2000; i++) { const v = R.randInt(n); assert.ok(Number.isInteger(v) && v >= 0 && v < n); }
});
function chi(n, draws) { const c = new Array(n).fill(0); for (let i = 0; i < draws; i++) c[R.randInt(n)]++; const e = draws / n; return c.reduce((s, x) => s + (x - e) ** 2 / e, 0); }
// 99.9th percentile chi-square: df=5 -> 20.52, df=9 -> 27.88. A sanity check, not a proof.
test('distribution sanity n = 6 (1e6 draws)', () => { assert.ok(chi(6, 1e6) < 20.52); });
test('distribution sanity n = 10 (1e6 draws)', () => { assert.ok(chi(10, 1e6) < 27.88); });
test('shuffle is a permutation and does not mutate input', () => {
  const a = [1, 2, 3, 4, 5, 6, 7]; const s = R.shuffle(a); assert.deepEqual([...s].sort(), a); assert.deepEqual(a, [1, 2, 3, 4, 5, 6, 7]);
});
