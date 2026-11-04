# Run: 2B/math500/A64x3T0_8k_q8

```json
{
  "name": "A64x3T0_8k_q8",
  "model": "2B",
  "task": "math500",
  "gguf": "gguf/2B_A64x3T0-q8_0.gguf",
  "preset": "qwen",
  "sampling": {
    "temperature": 1.0,
    "top_p": 0.95,
    "top_k": 20,
    "min_p": 0.0,
    "presence_penalty": 1.5
  },
  "n": 100,
  "max_tokens": 8192,
  "think": true,
  "seed": 0,
  "first": 0,
  "backend_sampling": true,
  "acc": 0.45,
  "truncated": 0.55,
  "acc_when_finished": 0.9778,
  "n_finished": 45,
  "mean_tokens": 6407,
  "mean_waits_per_kchar": 0.112
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 5319 | 0.13 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 8192 | 0.092 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 3408 | 0.092 | `6+9i` | `6+9i` |
| [algebra_1143](algebra_1143.md) | 5 | n | length | 8192 | 0.052 | `17` | `None` |
| [algebra_1184](algebra_1184.md) | 4 | n | length | 8192 | 0.134 | `129` | `None` |
| [algebra_1255](algebra_1255.md) | 2 | n | length | 8192 | 0.042 | `6` | `None` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 1695 | 0.0 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1275](algebra_1275.md) | 3 | n | length | 8192 | 0.044 | `\frac{\sqrt{3}}{3}` | `None` |
| [algebra_1332](algebra_1332.md) | 3 | Y | stop | 2342 | 0.0 | `9` | `9` |
| [algebra_1339](algebra_1339.md) | 5 | Y | stop | 8180 | 0.0 | `600` | `600` |
| [algebra_170](algebra_170.md) | 3 | Y | stop | 2243 | 0.0 | `11` | `11` |
| [algebra_187](algebra_187.md) | 4 | Y | stop | 6584 | 0.0 | `3` | `3` |
| [algebra_1934](algebra_1934.md) | 4 | Y | stop | 3133 | 0.0 | `13` | `13` |
| [algebra_2043](algebra_2043.md) | 5 | Y | stop | 3536 | 0.098 | `(-\infty, 2) \cup (3, \infty)` | `(-\infty, 2) \cup (3, \infty)` |
| [algebra_2064](algebra_2064.md) | 5 | Y | stop | 4543 | 0.0 | `81` | `81` |
| [algebra_224](algebra_224.md) | 4 | Y | stop | 2413 | 0.0 | `8` | `8` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 8192 | 0.247 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 8192 | 0.088 | `10` | `None` |
| [algebra_251](algebra_251.md) | 2 | Y | stop | 4092 | 0.0 | `2` | `2` |
| [algebra_2517](algebra_2517.md) | 5 | n | length | 8192 | 0.131 | `-\frac{35}{9}` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 8192 | 0.096 | `2107` | `14` |
| [algebra_2593](algebra_2593.md) | 2 | Y | stop | 4681 | 0.189 | `8000` | `8000` |
| [algebra_276](algebra_276.md) | 2 | Y | stop | 5495 | 0.077 | `12` | `12` |
| [algebra_297](algebra_297.md) | 5 | n | length | 8192 | 0.232 | `1736` | `None` |
| [algebra_305](algebra_305.md) | 5 | n | length | 8192 | 0.041 | `5` | `None` |
| [algebra_634](algebra_634.md) | 3 | Y | stop | 6929 | 0.177 | `4` | `4` |
| [algebra_661](algebra_661.md) | 3 | n | length | 8192 | 0.106 | `36` | `None` |
| [algebra_668](algebra_668.md) | 4 | Y | stop | 4003 | 0.087 | `45` | `45` |
| [algebra_694](algebra_694.md) | 3 | Y | stop | 3056 | 0.0 | `16` | `16` |
| [algebra_824](algebra_824.md) | 4 | Y | stop | 7986 | 0.094 | `12` | `12` |
| [algebra_907](algebra_907.md) | 4 | Y | stop | 4901 | 0.076 | `2` | `2` |
| [algebra_972](algebra_972.md) | 4 | n | length | 8192 | 0.053 | `\frac{11}{2}` | `None` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | Y | stop | 7140 | 0.105 | `\frac{11}{36}` | `\frac{11}{36}` |
| [counting_and_probability_134](counting_and_probability_134.md) | 4 | n | length | 8192 | 0.069 | `720` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 2164 | 0.0 | `6` | `6` |
| [counting_and_probability_199](counting_and_probability_199.md) | 2 | n | length | 8192 | 0.073 | `13` | `None` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 4347 | 0.074 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 1206 | 0.0 | `28` | `28` |
| [counting_and_probability_71](counting_and_probability_71.md) | 3 | n | length | 8192 | 0.077 | `3` | `None` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | Y | stop | 3873 | 0.0 | `\frac{1}{4}` | `\frac{1}{4}` |
| [geometry_106](geometry_106.md) | 2 | Y | stop | 4049 | 0.0 | `31` | `31` |
| [geometry_347](geometry_347.md) | 3 | Y | stop | 5916 | 0.207 | `76^\circ` | `76` |
| [geometry_456](geometry_456.md) | 2 | Y | stop | 4671 | 0.0 | `3` | `3` |
| [geometry_547](geometry_547.md) | 4 | n | length | 8192 | 0.078 | `54` | `None` |
| [geometry_627](geometry_627.md) | 4 | n | length | 8192 | 0.18 | `17` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 8192 | 0.161 | `1+2\sqrt{3}` | `None` |
| [geometry_802](geometry_802.md) | 2 | Y | stop | 4584 | 0.336 | `12` | `12` |
| [geometry_880](geometry_880.md) | 5 | n | length | 8192 | 0.102 | `2\sqrt{113}` | `None` |
| [geometry_947](geometry_947.md) | 5 | n | length | 8192 | 0.0 | `-\frac{24}{25}` | `None` |
| [geometry_967](geometry_967.md) | 3 | n | length | 8192 | 0.108 | `72` | `None` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 8192 | 0.173 | `-2,1` | `None` |
| [intermediate_algebra_117](intermediate_algebra_117.md) | 5 | n | length | 8192 | 0.115 | `15` | `None` |
| [intermediate_algebra_1217](intermediate_algebra_1217.md) | 2 | n | length | 8192 | 0.048 | `x^5 - x^4 + x^3 - x^2 + x - 1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 8192 | 0.251 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1365](intermediate_algebra_1365.md) | 3 | n | length | 8192 | 0.098 | `15` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 8192 | 0.197 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 8192 | 0.292 | `331` | `None` |
| [intermediate_algebra_1510](intermediate_algebra_1510.md) | 5 | n | length | 8192 | 0.574 | `0` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 8192 | 0.534 | `27648` | `None` |
| [intermediate_algebra_1714](intermediate_algebra_1714.md) | 1 | Y | stop | 2427 | 0.0 | `(5,\infty)` | `(5, \infty)` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 8192 | 0.168 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 8192 | 0.187 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_2015](intermediate_algebra_2015.md) | 5 | n | length | 8192 | 0.323 | `\{1\pm\sqrt{5},-2\}` | `None` |
| [intermediate_algebra_2146](intermediate_algebra_2146.md) | 4 | n | length | 8192 | 0.151 | `406` | `None` |
| [intermediate_algebra_362](intermediate_algebra_362.md) | 4 | n | length | 8192 | 0.057 | `40` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | Y | length | 8192 | 0.095 | `9` | `9` |
| [intermediate_algebra_960](intermediate_algebra_960.md) | 5 | n | length | 8192 | 0.122 | `\frac{17}{21}` | `None` |
| [number_theory_1002](number_theory_1002.md) | 5 | n | length | 8192 | 0.0 | `1440` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 8192 | 0.0 | `203` | `None` |
| [number_theory_1287](number_theory_1287.md) | 4 | Y | stop | 6965 | 0.0 | `8` | `8` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 8192 | 0.329 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 8192 | 0.047 | `1030` | `None` |
| [number_theory_686](number_theory_686.md) | 2 | Y | stop | 3535 | 0.317 | `4` | `4` |
| [number_theory_691](number_theory_691.md) | 3 | Y | stop | 5886 | 0.0 | `255` | `255` |
| [number_theory_72](number_theory_72.md) | 4 | Y | stop | 3745 | 0.103 | `121` | `121` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 8192 | 0.149 | `6` | `None` |
| [number_theory_931](number_theory_931.md) | 2 | n | length | 8192 | 0.044 | `49` | `None` |
| [prealgebra_1003](prealgebra_1003.md) | 5 | n | length | 8192 | 0.066 | `\frac{270}7\text{ degrees}` | `None` |
| [prealgebra_105](prealgebra_105.md) | 1 | Y | stop | 8118 | 0.15 | `\text{east}` | `east` |
| [prealgebra_1114](prealgebra_1114.md) | 2 | n | length | 8192 | 0.076 | `15\mbox{ cm}^2` | `None` |
| [prealgebra_1203](prealgebra_1203.md) | 5 | Y | stop | 4584 | 0.351 | `\$36` | `36` |
| [prealgebra_1227](prealgebra_1227.md) | 3 | Y | stop | 3644 | 0.0 | `60` | `60` |
| [prealgebra_1238](prealgebra_1238.md) | 3 | n | length | 8192 | 0.303 | `2` | `None` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 8192 | 0.251 | `8` | `None` |
| [prealgebra_1302](prealgebra_1302.md) | 4 | Y | stop | 1289 | 0.0 | `11\sqrt2` | `11\sqrt{2}` |
| [prealgebra_1423](prealgebra_1423.md) | 5 | n | stop | 3969 | 0.076 | `12\pi` | `12\pi \text{ (, approximately } 37.70)` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | Y | stop | 5505 | 0.0 | `4` | `4` |
| [prealgebra_1742](prealgebra_1742.md) | 3 | Y | stop | 3130 | 0.215 | `\dfrac{33}{100}` | `\frac{33}{100}` |
| [prealgebra_1807](prealgebra_1807.md) | 3 | n | length | 8192 | 0.042 | `120` | `None` |
| [prealgebra_2019](prealgebra_2019.md) | 2 | Y | stop | 3381 | 0.19 | `4.5` | `4.5` |
| [prealgebra_2057](prealgebra_2057.md) | 4 | Y | stop | 1827 | 0.0 | `90` | `90` |
| [prealgebra_996](prealgebra_996.md) | 1 | Y | stop | 1788 | 0.0 | `9` | `9` |
| [precalculus_285](precalculus_285.md) | 2 | n | length | 8192 | 0.057 | `6` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 5224 | 0.274 | `(15,-29)` | `(15, -29)` |
| [precalculus_580](precalculus_580.md) | 3 | n | length | 8192 | 0.103 | `120^\circ` | `None` |
| [precalculus_807](precalculus_807.md) | 2 | Y | stop | 2671 | 0.124 | `\left( 3, \frac{\pi}{2} \right)` | `(3, \frac{\pi}{2})` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 8192 | 0.055 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 8192 | 0.167 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
| [precalculus_927](precalculus_927.md) | 4 | n | length | 8192 | 0.142 | `90^\circ` | `None` |
| [precalculus_96](precalculus_96.md) | 3 | n | length | 8192 | 0.219 | `\frac{7}{4}` | `None` |
