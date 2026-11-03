# Run: A64x3_q8

```json
{
  "name": "A64x3_q8",
  "gguf": "gguf/A64x3-q8_0.gguf",
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
  "acc": 0.325,
  "truncated": 0.675,
  "acc_when_finished": 1.0,
  "n_finished": 13,
  "mean_tokens": 13957,
  "mean_waits_per_kchar": 0.109
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 15618 | 0.237 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 16384 | 0.162 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 6200 | 0.05 | `6+9i` | `6+9i` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 15810 | 0.058 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1339](algebra_1339.md) | 5 | Y | stop | 10432 | 0.103 | `600` | `600` |
| [algebra_170](algebra_170.md) | 3 | Y | stop | 7455 | 0.053 | `11` | `11` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 16384 | 0.157 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | Y | stop | 8612 | 0.158 | `10` | `10` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 16384 | 0.098 | `2107` | `None` |
| [algebra_276](algebra_276.md) | 2 | n | length | 16384 | 0.156 | `12` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | length | 16384 | 0.069 | `36` | `None` |
| [algebra_694](algebra_694.md) | 3 | n | length | 16384 | 0.022 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 16384 | 0.075 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | n | length | 16384 | 0.053 | `2` | `None` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 16384 | 0.045 | `\frac{11}{36}` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 5255 | 0.108 | `6` | `6` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 5029 | 0.065 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 8458 | 0.031 | `28` | `28` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 16384 | 0.083 | `\frac{1}{4}` | `None` |
| [geometry_347](geometry_347.md) | 3 | Y | stop | 3349 | 0.088 | `76^\circ` | `76` |
| [geometry_711](geometry_711.md) | 5 | n | length | 16384 | 0.118 | `1+2\sqrt{3}` | `None` |
| [geometry_967](geometry_967.md) | 3 | Y | stop | 11693 | 0.047 | `72` | `72` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 16384 | 0.304 | `-2,1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 16384 | 0.168 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 16384 | 0.061 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 16384 | 0.027 | `331` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 16384 | 0.167 | `27648` | `None` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 16384 | 0.133 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 16384 | 0.356 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | Y | stop | 15916 | 0.079 | `9` | `9` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 16384 | 0.035 | `203` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 16384 | 0.374 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 16384 | 0.251 | `1030` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 16384 | 0.034 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 16384 | 0.118 | `6` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 16384 | 0.077 | `8` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 16384 | 0.0 | `4` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 2093 | 0.0 | `(15,-29)` | `(15, -29)` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 16384 | 0.027 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 16384 | 0.115 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
