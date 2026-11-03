# Run: 0.8B/math500/base_32k_q8

```json
{
  "name": "base_32k_q8",
  "gguf": "gguf/original-q8_0.gguf",
  "preset": "qwen",
  "sampling": {
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 20,
    "min_p": 0.0,
    "presence_penalty": 1.5
  },
  "n": 100,
  "max_tokens": 32768,
  "think": true,
  "seed": 0,
  "first": 0,
  "backend_sampling": true,
  "acc": 0.15,
  "truncated": 0.88,
  "acc_when_finished": 1.0,
  "n_finished": 12,
  "mean_tokens": 30971,
  "mean_waits_per_kchar": 3.803
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 23505 | 3.198 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 32768 | 4.796 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 19874 | 2.307 | `6+9i` | `6+9i` |
| [algebra_1143](algebra_1143.md) | 5 | n | length | 32768 | 5.041 | `17` | `None` |
| [algebra_1184](algebra_1184.md) | 4 | n | length | 32768 | 3.306 | `129` | `None` |
| [algebra_1255](algebra_1255.md) | 2 | Y | stop | 8802 | 2.713 | `6` | `6` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 20244 | 3.303 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1275](algebra_1275.md) | 3 | n | length | 32768 | 5.237 | `\frac{\sqrt{3}}{3}` | `None` |
| [algebra_1332](algebra_1332.md) | 3 | n | length | 32768 | 3.229 | `9` | `None` |
| [algebra_1339](algebra_1339.md) | 5 | n | length | 32768 | 2.347 | `600` | `None` |
| [algebra_170](algebra_170.md) | 3 | n | length | 32768 | 5.789 | `11` | `None` |
| [algebra_187](algebra_187.md) | 4 | n | length | 32768 | 5.237 | `3` | `None` |
| [algebra_1934](algebra_1934.md) | 4 | Y | length | 32768 | 3.013 | `13` | `13` |
| [algebra_2043](algebra_2043.md) | 5 | n | length | 32768 | 5.644 | `(-\infty, 2) \cup (3, \infty)` | `None` |
| [algebra_2064](algebra_2064.md) | 5 | n | length | 32768 | 1.353 | `81` | `None` |
| [algebra_224](algebra_224.md) | 4 | n | length | 32768 | 4.835 | `8` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 32768 | 4.09 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 32768 | 5.119 | `10` | `None` |
| [algebra_251](algebra_251.md) | 2 | n | length | 32768 | 4.052 | `2` | `None` |
| [algebra_2517](algebra_2517.md) | 5 | n | length | 32768 | 5.725 | `-\frac{35}{9}` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 32768 | 4.388 | `2107` | `None` |
| [algebra_2593](algebra_2593.md) | 2 | Y | stop | 14383 | 2.328 | `8000` | `8000` |
| [algebra_276](algebra_276.md) | 2 | n | length | 32768 | 4.333 | `12` | `None` |
| [algebra_297](algebra_297.md) | 5 | n | length | 32768 | 3.941 | `1736` | `None` |
| [algebra_305](algebra_305.md) | 5 | n | length | 32768 | 4.882 | `5` | `None` |
| [algebra_634](algebra_634.md) | 3 | n | length | 32768 | 3.924 | `4` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | length | 32768 | 5.096 | `36` | `None` |
| [algebra_668](algebra_668.md) | 4 | Y | stop | 32737 | 3.336 | `45` | `45` |
| [algebra_694](algebra_694.md) | 3 | n | length | 32768 | 3.213 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 32768 | 5.537 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | n | length | 32768 | 3.977 | `2` | `None` |
| [algebra_972](algebra_972.md) | 4 | n | length | 32768 | 3.995 | `\frac{11}{2}` | `None` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 32768 | 1.877 | `\frac{11}{36}` | `None` |
| [counting_and_probability_134](counting_and_probability_134.md) | 4 | n | length | 32768 | 4.411 | `720` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | length | 32768 | 3.891 | `6` | `6` |
| [counting_and_probability_199](counting_and_probability_199.md) | 2 | n | length | 32768 | 3.747 | `13` | `None` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | n | length | 32768 | 2.603 | `210` | `None` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 8324 | 1.61 | `28` | `28` |
| [counting_and_probability_71](counting_and_probability_71.md) | 3 | n | length | 32768 | 3.779 | `3` | `None` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 32768 | 1.485 | `\frac{1}{4}` | `None` |
| [geometry_106](geometry_106.md) | 2 | Y | length | 32768 | 2.454 | `31` | `31` |
| [geometry_347](geometry_347.md) | 3 | n | length | 32768 | 2.232 | `76^\circ` | `None` |
| [geometry_456](geometry_456.md) | 2 | n | length | 32768 | 3.39 | `3` | `None` |
| [geometry_547](geometry_547.md) | 4 | n | length | 32768 | 3.232 | `54` | `None` |
| [geometry_627](geometry_627.md) | 4 | n | length | 32768 | 3.453 | `17` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 32768 | 3.41 | `1+2\sqrt{3}` | `None` |
| [geometry_802](geometry_802.md) | 2 | n | length | 32768 | 4.641 | `12` | `None` |
| [geometry_880](geometry_880.md) | 5 | n | length | 32768 | 3.893 | `2\sqrt{113}` | `None` |
| [geometry_947](geometry_947.md) | 5 | n | length | 32768 | 3.719 | `-\frac{24}{25}` | `None` |
| [geometry_967](geometry_967.md) | 3 | Y | stop | 28418 | 2.328 | `72` | `72` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 32768 | 4.788 | `-2,1` | `None` |
| [intermediate_algebra_117](intermediate_algebra_117.md) | 5 | n | length | 32768 | 5.265 | `15` | `None` |
| [intermediate_algebra_1217](intermediate_algebra_1217.md) | 2 | n | length | 32768 | 3.119 | `x^5 - x^4 + x^3 - x^2 + x - 1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 32768 | 5.368 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1365](intermediate_algebra_1365.md) | 3 | n | length | 32768 | 4.954 | `15` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 32768 | 5.786 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 32768 | 4.066 | `331` | `None` |
| [intermediate_algebra_1510](intermediate_algebra_1510.md) | 5 | n | length | 32768 | 6.609 | `0` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 32768 | 4.912 | `27648` | `None` |
| [intermediate_algebra_1714](intermediate_algebra_1714.md) | 1 | n | length | 32768 | 4.742 | `(5,\infty)` | `None` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 32768 | 3.122 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 32768 | 5.954 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_2015](intermediate_algebra_2015.md) | 5 | n | length | 32768 | 4.469 | `\{1\pm\sqrt{5},-2\}` | `None` |
| [intermediate_algebra_2146](intermediate_algebra_2146.md) | 4 | n | length | 32768 | 4.973 | `406` | `None` |
| [intermediate_algebra_362](intermediate_algebra_362.md) | 4 | n | length | 32768 | 5.194 | `40` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 32768 | 4.734 | `9` | `None` |
| [intermediate_algebra_960](intermediate_algebra_960.md) | 5 | n | length | 32768 | 5.135 | `\frac{17}{21}` | `None` |
| [number_theory_1002](number_theory_1002.md) | 5 | n | length | 32768 | 5.298 | `1440` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 32768 | 2.957 | `203` | `None` |
| [number_theory_1287](number_theory_1287.md) | 4 | n | length | 32768 | 4.406 | `8` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 32768 | 3.629 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 32768 | 4.47 | `1030` | `None` |
| [number_theory_686](number_theory_686.md) | 2 | n | length | 32768 | 5.461 | `4` | `None` |
| [number_theory_691](number_theory_691.md) | 3 | n | length | 32768 | 2.921 | `255` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 32768 | 3.357 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 32768 | 5.551 | `6` | `None` |
| [number_theory_931](number_theory_931.md) | 2 | n | length | 32768 | 2.298 | `49` | `None` |
| [prealgebra_1003](prealgebra_1003.md) | 5 | n | length | 32768 | 3.382 | `\frac{270}7\text{ degrees}` | `None` |
| [prealgebra_105](prealgebra_105.md) | 1 | n | length | 32768 | 2.073 | `\text{east}` | `None` |
| [prealgebra_1114](prealgebra_1114.md) | 2 | n | length | 32768 | 4.229 | `15\mbox{ cm}^2` | `None` |
| [prealgebra_1203](prealgebra_1203.md) | 5 | n | length | 32768 | 1.712 | `\$36` | `None` |
| [prealgebra_1227](prealgebra_1227.md) | 3 | n | length | 32768 | 3.09 | `60` | `None` |
| [prealgebra_1238](prealgebra_1238.md) | 3 | n | length | 32768 | 3.447 | `2` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 32768 | 3.887 | `8` | `None` |
| [prealgebra_1302](prealgebra_1302.md) | 4 | n | length | 32768 | 2.789 | `11\sqrt2` | `None` |
| [prealgebra_1423](prealgebra_1423.md) | 5 | n | length | 32768 | 1.871 | `12\pi` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 32768 | 2.431 | `4` | `None` |
| [prealgebra_1742](prealgebra_1742.md) | 3 | n | length | 32768 | 4.31 | `\dfrac{33}{100}` | `None` |
| [prealgebra_1807](prealgebra_1807.md) | 3 | n | length | 32768 | 2.742 | `120` | `None` |
| [prealgebra_2019](prealgebra_2019.md) | 2 | Y | stop | 18721 | 3.171 | `4.5` | `4.5` |
| [prealgebra_2057](prealgebra_2057.md) | 4 | n | length | 32768 | 2.444 | `90` | `None` |
| [prealgebra_996](prealgebra_996.md) | 1 | Y | stop | 21731 | 3.096 | `9` | `9` |
| [precalculus_285](precalculus_285.md) | 2 | n | length | 32768 | 4.759 | `6` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 5288 | 1.716 | `(15,-29)` | `(15, -29)` |
| [precalculus_580](precalculus_580.md) | 3 | n | length | 32768 | 3.7 | `120^\circ` | `None` |
| [precalculus_807](precalculus_807.md) | 2 | Y | stop | 11459 | 2.068 | `\left( 3, \frac{\pi}{2} \right)` | `(3, \frac{\pi}{2})` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 32768 | 3.211 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 32768 | 2.533 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
| [precalculus_927](precalculus_927.md) | 4 | n | length | 32768 | 4.688 | `90^\circ` | `None` |
| [precalculus_96](precalculus_96.md) | 3 | n | length | 32768 | 3.995 | `\frac{7}{4}` | `None` |
