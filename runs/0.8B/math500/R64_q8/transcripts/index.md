# Run: 0.8B/math500/R64_q8

```json
{
  "name": "R64_q8",
  "gguf": "gguf/R64-q8_0.gguf",
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
  "acc": 0.1,
  "truncated": 0.9,
  "acc_when_finished": 1.0,
  "n_finished": 4,
  "mean_tokens": 15605,
  "mean_waits_per_kchar": 3.474
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | n | length | 16384 | 4.216 | `\frac{11}{2}` | `None` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 16384 | 3.069 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 11155 | 2.019 | `6+9i` | `6+9i` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 12835 | 2.304 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1339](algebra_1339.md) | 5 | n | length | 16384 | 2.258 | `600` | `None` |
| [algebra_170](algebra_170.md) | 3 | n | length | 16384 | 3.53 | `11` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 16384 | 4.39 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 16384 | 4.099 | `10` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 16384 | 3.902 | `2107` | `None` |
| [algebra_276](algebra_276.md) | 2 | n | length | 16384 | 4.881 | `12` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | length | 16384 | 2.515 | `36` | `None` |
| [algebra_694](algebra_694.md) | 3 | n | length | 16384 | 3.294 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 16384 | 5.382 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | n | length | 16384 | 4.536 | `2` | `None` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 16384 | 4.418 | `\frac{11}{36}` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | n | length | 16384 | 2.6 | `6` | `None` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | n | length | 16384 | 2.096 | `210` | `None` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 7132 | 0.858 | `28` | `28` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 16384 | 2.22 | `\frac{1}{4}` | `None` |
| [geometry_347](geometry_347.md) | 3 | n | length | 16384 | 2.219 | `76^\circ` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 16384 | 2.581 | `1+2\sqrt{3}` | `None` |
| [geometry_967](geometry_967.md) | 3 | n | length | 16384 | 2.206 | `72` | `None` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 16384 | 4.324 | `-2,1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 16384 | 4.672 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 16384 | 3.741 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 16384 | 4.94 | `331` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 16384 | 5.116 | `27648` | `None` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 16384 | 3.463 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 16384 | 5.671 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 16384 | 5.202 | `9` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 16384 | 2.836 | `203` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 16384 | 3.53 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 16384 | 3.621 | `1030` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 16384 | 2.626 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 16384 | 4.711 | `6` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 16384 | 3.234 | `8` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 16384 | 3.481 | `4` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 3258 | 0.898 | `(15,-29)` | `(15, -29)` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 16384 | 3.823 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 16384 | 3.468 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
