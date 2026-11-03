# Run: A64VP_q8

```json
{
  "name": "A64VP_q8",
  "gguf": "gguf/A64VP-q8_0.gguf",
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
  "mean_tokens": 14538,
  "mean_waits_per_kchar": 0.461
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 15772 | 0.421 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 16384 | 0.436 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 8773 | 0.529 | `6+9i` | `6 + 9i` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 9163 | 0.209 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1339](algebra_1339.md) | 5 | n | length | 16384 | 0.426 | `600` | `None` |
| [algebra_170](algebra_170.md) | 3 | n | length | 16384 | 0.34 | `11` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 16384 | 0.441 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 16384 | 0.456 | `10` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 16384 | 0.657 | `2107` | `None` |
| [algebra_276](algebra_276.md) | 2 | n | length | 16384 | 0.382 | `12` | `3` |
| [algebra_661](algebra_661.md) | 3 | n | length | 16384 | 0.307 | `36` | `None` |
| [algebra_694](algebra_694.md) | 3 | n | length | 16384 | 0.277 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 16384 | 0.525 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | Y | stop | 11484 | 0.599 | `2` | `2` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 16384 | 0.179 | `\frac{11}{36}` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 7396 | 0.437 | `6` | `6` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 9357 | 0.448 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 11707 | 0.179 | `28` | `28` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | Y | stop | 15391 | 0.245 | `\frac{1}{4}` | `\frac{1}{4}` |
| [geometry_347](geometry_347.md) | 3 | Y | stop | 10652 | 0.189 | `76^\circ` | `76` |
| [geometry_711](geometry_711.md) | 5 | n | length | 16384 | 0.667 | `1+2\sqrt{3}` | `None` |
| [geometry_967](geometry_967.md) | 3 | n | length | 16384 | 0.265 | `72` | `None` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 16384 | 0.77 | `-2,1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 16384 | 0.61 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 16384 | 0.228 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 16384 | 0.456 | `331` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 16384 | 0.629 | `27648` | `None` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 16384 | 0.448 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 16384 | 0.789 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 16384 | 0.999 | `9` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 16384 | 0.138 | `203` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 16384 | 0.405 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 16384 | 1.462 | `1030` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 16384 | 0.202 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 16384 | 0.461 | `6` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 16384 | 0.272 | `8` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | Y | stop | 4468 | 0.476 | `4` | `4` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 2211 | 0.491 | `(15,-29)` | `(15, -29)` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 16384 | 0.244 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 16384 | 0.737 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
