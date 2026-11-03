# Run: Dfull_q8

```json
{
  "name": "Dfull_q8",
  "gguf": "gguf/D_full-q8_0.gguf",
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
  "acc": 0.125,
  "truncated": 0.875,
  "acc_when_finished": 1.0,
  "n_finished": 5,
  "mean_tokens": 15567,
  "mean_waits_per_kchar": 2.765
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | n | length | 16384 | 2.774 | `\frac{11}{2}` | `None` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 16384 | 3.989 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 12327 | 2.184 | `6+9i` | `6+9i` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 11862 | 2.308 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1339](algebra_1339.md) | 5 | n | length | 16384 | 2.231 | `600` | `None` |
| [algebra_170](algebra_170.md) | 3 | n | length | 16384 | 2.048 | `11` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 16384 | 3.718 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 16384 | 3.029 | `10` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 16384 | 3.521 | `2107` | `None` |
| [algebra_276](algebra_276.md) | 2 | n | length | 16384 | 3.935 | `12` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | length | 16384 | 2.079 | `36` | `None` |
| [algebra_694](algebra_694.md) | 3 | n | length | 16384 | 2.972 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 16384 | 3.316 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | n | length | 16384 | 3.028 | `2` | `None` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 16384 | 2.097 | `\frac{11}{36}` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 12682 | 1.773 | `6` | `6` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 8493 | 1.035 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | n | length | 16384 | 2.029 | `28` | `None` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 16384 | 2.44 | `\frac{1}{4}` | `None` |
| [geometry_347](geometry_347.md) | 3 | n | length | 16384 | 2.637 | `76^\circ` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 16384 | 2.32 | `1+2\sqrt{3}` | `None` |
| [geometry_967](geometry_967.md) | 3 | n | length | 16384 | 1.729 | `72` | `None` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 16384 | 3.262 | `-2,1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 16384 | 4.138 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 16384 | 2.836 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 16384 | 3.485 | `331` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 16384 | 3.466 | `27648` | `None` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 16384 | 2.229 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 16384 | 3.835 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 16384 | 4.747 | `9` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 16384 | 1.215 | `203` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 16384 | 3.391 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 16384 | 3.181 | `1030` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 16384 | 1.802 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 16384 | 3.493 | `6` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 16384 | 1.883 | `8` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 16384 | 3.676 | `4` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 3881 | 1.097 | `(15,-29)` | `(15, -29)` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 16384 | 2.487 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 16384 | 3.186 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
