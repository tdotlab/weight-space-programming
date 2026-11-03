# Run: A64_q8

```json
{
  "name": "A64_q8",
  "gguf": "gguf/A64-q8_0.gguf",
  "preset": "qwen",
  "sampling": {
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 20,
    "min_p": 0.0,
    "presence_penalty": 1.5
  },
  "n": 40,
  "max_tokens": 16384,
  "think": true,
  "seed": 0,
  "first": 40,
  "backend_sampling": true,
  "acc": 0.275,
  "truncated": 0.725,
  "acc_when_finished": 1.0,
  "n_finished": 11,
  "mean_tokens": 14590,
  "mean_waits_per_kchar": 0.403
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 12269 | 0.388 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 16384 | 0.518 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 5716 | 0.381 | `6+9i` | `6+9i` |
| [algebra_1265](algebra_1265.md) | 2 | n | length | 16384 | 0.163 | `\frac{3}{2}` | `None` |
| [algebra_1339](algebra_1339.md) | 5 | Y | stop | 10327 | 0.238 | `600` | `600` |
| [algebra_170](algebra_170.md) | 3 | n | length | 16384 | 0.709 | `11` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 16384 | 0.321 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | Y | stop | 9601 | 0.213 | `10` | `10` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 16384 | 0.53 | `2107` | `None` |
| [algebra_276](algebra_276.md) | 2 | Y | stop | 10179 | 0.325 | `12` | `12` |
| [algebra_661](algebra_661.md) | 3 | n | length | 16384 | 0.205 | `36` | `None` |
| [algebra_694](algebra_694.md) | 3 | n | length | 16384 | 0.195 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 16384 | 0.468 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | Y | stop | 9224 | 0.548 | `2` | `2` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 16384 | 0.272 | `\frac{11}{36}` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 9864 | 0.259 | `6` | `6` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 15178 | 0.318 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 13996 | 0.111 | `28` | `28` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 16384 | 0.207 | `\frac{1}{4}` | `None` |
| [geometry_347](geometry_347.md) | 3 | Y | stop | 6186 | 0.046 | `76^\circ` | `76` |
| [geometry_711](geometry_711.md) | 5 | n | length | 16384 | 0.332 | `1+2\sqrt{3}` | `None` |
| [geometry_967](geometry_967.md) | 3 | n | length | 16384 | 0.271 | `72` | `None` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 16384 | 0.647 | `-2,1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 16384 | 0.988 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 16384 | 0.476 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 16384 | 0.91 | `331` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 16384 | 0.684 | `27648` | `None` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 16384 | 0.262 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 16384 | 0.76 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 16384 | 0.302 | `9` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 16384 | 0.166 | `203` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 16384 | 0.336 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 16384 | 0.961 | `1030` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 16384 | 0.315 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 16384 | 0.381 | `6` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 16384 | 0.092 | `8` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 16384 | 0.192 | `4` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 5931 | 0.761 | `(15,-29)` | `(15, -29)` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 16384 | 0.453 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 16384 | 0.421 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
