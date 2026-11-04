# Run: 0.8B/math500/A64x3Fh_q8

```json
{
  "name": "A64x3Fh_q8",
  "model": "0.8B",
  "task": "math500",
  "gguf": "gguf/A64x3Fh-q8_0.gguf",
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
  "mean_tokens": 14548,
  "mean_waits_per_kchar": 0.11
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 11957 | 0.19 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 16384 | 0.183 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 5407 | 0.118 | `6+9i` | `6+9i` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 9083 | 0.035 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1339](algebra_1339.md) | 5 | Y | stop | 13172 | 0.085 | `600` | `600` |
| [algebra_170](algebra_170.md) | 3 | n | length | 16384 | 0.122 | `11` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 16384 | 0.157 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 16384 | 0.021 | `10` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 16384 | 0.146 | `2107` | `None` |
| [algebra_276](algebra_276.md) | 2 | n | length | 16384 | 0.147 | `12` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | length | 16384 | 0.161 | `36` | `None` |
| [algebra_694](algebra_694.md) | 3 | n | length | 16384 | 0.117 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | Y | stop | 15690 | 0.073 | `12` | `12` |
| [algebra_907](algebra_907.md) | 4 | Y | stop | 16112 | 0.094 | `2` | `2` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 16384 | 0.022 | `\frac{11}{36}` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 12549 | 0.07 | `6` | `6` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 2439 | 0.0 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 4779 | 0.057 | `28` | `28` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 16384 | 0.086 | `\frac{1}{4}` | `None` |
| [geometry_347](geometry_347.md) | 3 | Y | stop | 13938 | 0.061 | `76^\circ` | `76` |
| [geometry_711](geometry_711.md) | 5 | n | length | 16384 | 0.082 | `1+2\sqrt{3}` | `None` |
| [geometry_967](geometry_967.md) | 3 | n | length | 16384 | 0.016 | `72` | `None` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 16384 | 0.111 | `-2,1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 16384 | 0.075 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 16384 | 0.085 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 16384 | 0.216 | `331` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 16384 | 0.197 | `27648` | `None` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 16384 | 0.093 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 16384 | 0.283 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 16384 | 0.202 | `9` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 16384 | 0.034 | `203` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 16384 | 0.084 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 16384 | 0.396 | `1030` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 16384 | 0.018 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 16384 | 0.167 | `6` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 16384 | 0.064 | `8` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 16384 | 0.164 | `4` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 1654 | 0.0 | `(15,-29)` | `(15, -29)` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 16384 | 0.082 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 16384 | 0.082 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
