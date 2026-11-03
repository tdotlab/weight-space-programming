# Run: A64h_q8

```json
{
  "name": "A64h_q8",
  "gguf": "gguf/A64h-q8_0.gguf",
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
  "acc": 0.225,
  "truncated": 0.775,
  "acc_when_finished": 1.0,
  "n_finished": 9,
  "mean_tokens": 14972,
  "mean_waits_per_kchar": 1.179
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | n | length | 16384 | 1.383 | `\frac{11}{2}` | `None` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 16384 | 1.401 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 4317 | 0.988 | `6+9i` | `6+9i` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 10448 | 0.64 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1339](algebra_1339.md) | 5 | Y | stop | 12011 | 0.693 | `600` | `600` |
| [algebra_170](algebra_170.md) | 3 | n | length | 16384 | 1.671 | `11` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 16384 | 1.679 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | Y | stop | 15263 | 0.753 | `10` | `10` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 16384 | 1.601 | `2107` | `None` |
| [algebra_276](algebra_276.md) | 2 | n | length | 16384 | 1.386 | `12` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | length | 16384 | 0.904 | `36` | `None` |
| [algebra_694](algebra_694.md) | 3 | n | length | 16384 | 0.863 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 16384 | 1.07 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | n | length | 16384 | 1.352 | `2` | `None` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 16384 | 0.772 | `\frac{11}{36}` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 8774 | 0.874 | `6` | `6` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 9959 | 0.35 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 11527 | 0.441 | `28` | `28` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 16384 | 0.481 | `\frac{1}{4}` | `None` |
| [geometry_347](geometry_347.md) | 3 | n | length | 16384 | 1.277 | `76^\circ` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 16384 | 0.89 | `1+2\sqrt{3}` | `None` |
| [geometry_967](geometry_967.md) | 3 | Y | stop | 15446 | 0.582 | `72` | `72` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 16384 | 1.439 | `-2,1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 16384 | 1.758 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 16384 | 0.864 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 16384 | 1.57 | `331` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 16384 | 1.861 | `27648` | `None` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 16384 | 1.438 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 16384 | 2.328 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 16384 | 1.714 | `9` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 16384 | 0.716 | `203` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 16384 | 1.877 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 16384 | 1.576 | `1030` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 16384 | 0.818 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 16384 | 1.9 | `6` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 16384 | 1.057 | `8` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 16384 | 1.4 | `4` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 3243 | 0.521 | `(15,-29)` | `(15, -29)` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 16384 | 0.994 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 16384 | 1.271 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
