# Run: 0.8B/math500/A64x3_32k_q8

```json
{
  "name": "A64x3_32k_q8",
  "gguf": "gguf/A64x3-q8_0.gguf",
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
  "acc": 0.41,
  "truncated": 0.53,
  "acc_when_finished": 0.8723,
  "n_finished": 47,
  "mean_tokens": 24467,
  "mean_waits_per_kchar": 0.099
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 11013 | 0.203 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 32768 | 0.113 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 6464 | 0.0 | `6+9i` | `6 + 9i` |
| [algebra_1143](algebra_1143.md) | 5 | n | length | 32768 | 0.082 | `17` | `None` |
| [algebra_1184](algebra_1184.md) | 4 | n | length | 32768 | 0.047 | `129` | `None` |
| [algebra_1255](algebra_1255.md) | 2 | Y | stop | 4890 | 0.072 | `6` | `6` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 2872 | 0.0 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1275](algebra_1275.md) | 3 | n | length | 32768 | 0.083 | `\frac{\sqrt{3}}{3}` | `\sqrt{\frac{1}{3^6}} = (3^6)^{-1/2} = 3^{-3} = \frac{1}{3^3} = \frac{1}{27}.` |
| [algebra_1332](algebra_1332.md) | 3 | Y | stop | 18325 | 0.034 | `9` | `9` |
| [algebra_1339](algebra_1339.md) | 5 | Y | stop | 16246 | 0.094 | `600` | `600` |
| [algebra_170](algebra_170.md) | 3 | Y | stop | 28346 | 0.064 | `11` | `11` |
| [algebra_187](algebra_187.md) | 4 | n | length | 32768 | 0.16 | `3` | `None` |
| [algebra_1934](algebra_1934.md) | 4 | Y | stop | 22654 | 0.027 | `13` | `13` |
| [algebra_2043](algebra_2043.md) | 5 | n | stop | 10869 | 0.089 | `(-\infty, 2) \cup (3, \infty)` | `(-\infty, 2] \cup [3, \infty)` |
| [algebra_2064](algebra_2064.md) | 5 | n | length | 32768 | 0.014 | `81` | `None` |
| [algebra_224](algebra_224.md) | 4 | n | length | 32768 | 0.091 | `8` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 32768 | 0.094 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 32768 | 0.035 | `10` | `None` |
| [algebra_251](algebra_251.md) | 2 | Y | stop | 15568 | 0.069 | `2` | `2` |
| [algebra_2517](algebra_2517.md) | 5 | n | length | 32768 | 0.098 | `-\frac{35}{9}` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | Y | stop | 24827 | 0.064 | `2107` | `2107` |
| [algebra_2593](algebra_2593.md) | 2 | Y | stop | 6307 | 0.19 | `8000` | `8000` |
| [algebra_276](algebra_276.md) | 2 | Y | stop | 13739 | 0.058 | `12` | `12` |
| [algebra_297](algebra_297.md) | 5 | n | length | 32768 | 0.068 | `1736` | `None` |
| [algebra_305](algebra_305.md) | 5 | Y | stop | 29113 | 0.097 | `5` | `5` |
| [algebra_634](algebra_634.md) | 3 | n | length | 32768 | 0.125 | `4` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | stop | 31796 | 0.048 | `36` | `9` |
| [algebra_668](algebra_668.md) | 4 | Y | stop | 12819 | 0.0 | `45` | `45` |
| [algebra_694](algebra_694.md) | 3 | Y | stop | 8830 | 0.036 | `16` | `16` |
| [algebra_824](algebra_824.md) | 4 | Y | stop | 15605 | 0.048 | `12` | `12` |
| [algebra_907](algebra_907.md) | 4 | Y | stop | 10159 | 0.122 | `2` | `2` |
| [algebra_972](algebra_972.md) | 4 | Y | stop | 30802 | 0.155 | `\frac{11}{2}` | `\frac{11}{2}` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 32768 | 0.02 | `\frac{11}{36}` | `None` |
| [counting_and_probability_134](counting_and_probability_134.md) | 4 | n | length | 32768 | 0.132 | `720` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 4922 | 0.114 | `6` | `6` |
| [counting_and_probability_199](counting_and_probability_199.md) | 2 | n | length | 32768 | 0.155 | `13` | `None` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 4006 | 0.083 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 11938 | 0.066 | `28` | `28` |
| [counting_and_probability_71](counting_and_probability_71.md) | 3 | n | stop | 30298 | 0.069 | `3` | `15` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | Y | stop | 19703 | 0.079 | `\frac{1}{4}` | `\frac{1}{4}` |
| [geometry_106](geometry_106.md) | 2 | Y | stop | 4248 | 0.075 | `31` | `31` |
| [geometry_347](geometry_347.md) | 3 | Y | stop | 25193 | 0.011 | `76^\circ` | `76` |
| [geometry_456](geometry_456.md) | 2 | Y | stop | 3773 | 0.0 | `3` | `3` |
| [geometry_547](geometry_547.md) | 4 | n | length | 32768 | 0.139 | `54` | `None` |
| [geometry_627](geometry_627.md) | 4 | n | length | 32768 | 0.009 | `17` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 32768 | 0.04 | `1+2\sqrt{3}` | `None` |
| [geometry_802](geometry_802.md) | 2 | Y | stop | 9785 | 0.215 | `12` | `12` |
| [geometry_880](geometry_880.md) | 5 | n | length | 32768 | 0.078 | `2\sqrt{113}` | `None` |
| [geometry_947](geometry_947.md) | 5 | n | length | 32768 | 0.051 | `-\frac{24}{25}` | `None` |
| [geometry_967](geometry_967.md) | 3 | Y | stop | 15885 | 0.036 | `72` | `72` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | Y | stop | 15343 | 0.225 | `-2,1` | `1, -2` |
| [intermediate_algebra_117](intermediate_algebra_117.md) | 5 | n | length | 32768 | 0.121 | `15` | `None` |
| [intermediate_algebra_1217](intermediate_algebra_1217.md) | 2 | n | stop | 27081 | 0.098 | `x^5 - x^4 + x^3 - x^2 + x - 1` | `-2` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 32768 | 0.098 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1365](intermediate_algebra_1365.md) | 3 | Y | stop | 32515 | 0.05 | `15` | `15` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 32768 | 0.027 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 32768 | 0.125 | `331` | `None` |
| [intermediate_algebra_1510](intermediate_algebra_1510.md) | 5 | n | length | 32768 | 0.435 | `0` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 32768 | 0.168 | `27648` | `None` |
| [intermediate_algebra_1714](intermediate_algebra_1714.md) | 1 | Y | stop | 5953 | 0.051 | `(5,\infty)` | `(5, +\infty)` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 32768 | 0.104 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 32768 | 0.383 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_2015](intermediate_algebra_2015.md) | 5 | n | length | 32768 | 0.436 | `\{1\pm\sqrt{5},-2\}` | `None` |
| [intermediate_algebra_2146](intermediate_algebra_2146.md) | 4 | n | length | 32768 | 0.141 | `406` | `None` |
| [intermediate_algebra_362](intermediate_algebra_362.md) | 4 | n | length | 32768 | 0.074 | `40` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | Y | stop | 12397 | 0.2 | `9` | `9` |
| [intermediate_algebra_960](intermediate_algebra_960.md) | 5 | n | length | 32768 | 0.195 | `\frac{17}{21}` | `None` |
| [number_theory_1002](number_theory_1002.md) | 5 | n | length | 32768 | 0.076 | `1440` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 32768 | 0.051 | `203` | `None` |
| [number_theory_1287](number_theory_1287.md) | 4 | n | length | 32768 | 0.134 | `8` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 32768 | 0.1 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 32768 | 0.286 | `1030` | `None` |
| [number_theory_686](number_theory_686.md) | 2 | n | length | 32768 | 0.143 | `4` | `None` |
| [number_theory_691](number_theory_691.md) | 3 | n | length | 32768 | 0.108 | `255` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 32768 | 0.01 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 32768 | 0.044 | `6` | `None` |
| [number_theory_931](number_theory_931.md) | 2 | n | length | 32768 | 0.01 | `49` | `None` |
| [prealgebra_1003](prealgebra_1003.md) | 5 | n | length | 32768 | 0.145 | `\frac{270}7\text{ degrees}` | `None` |
| [prealgebra_105](prealgebra_105.md) | 1 | n | length | 32768 | 0.096 | `\text{east}` | `None` |
| [prealgebra_1114](prealgebra_1114.md) | 2 | Y | stop | 32658 | 0.131 | `15\mbox{ cm}^2` | `15` |
| [prealgebra_1203](prealgebra_1203.md) | 5 | n | length | 32768 | 0.056 | `\$36` | `None` |
| [prealgebra_1227](prealgebra_1227.md) | 3 | n | length | 32768 | 0.069 | `60` | `None` |
| [prealgebra_1238](prealgebra_1238.md) | 3 | Y | stop | 9251 | 0.158 | `2` | `2` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 32768 | 0.04 | `8` | `None` |
| [prealgebra_1302](prealgebra_1302.md) | 4 | Y | stop | 6486 | 0.054 | `11\sqrt2` | `11\sqrt{2}` |
| [prealgebra_1423](prealgebra_1423.md) | 5 | n | length | 32768 | 0.063 | `12\pi` | `9` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | Y | stop | 15727 | 0.0 | `4` | `4` |
| [prealgebra_1742](prealgebra_1742.md) | 3 | Y | stop | 4017 | 0.087 | `\dfrac{33}{100}` | `\frac{33}{100}` |
| [prealgebra_1807](prealgebra_1807.md) | 3 | n | length | 32768 | 0.028 | `120` | `None` |
| [prealgebra_2019](prealgebra_2019.md) | 2 | Y | stop | 7056 | 0.042 | `4.5` | `4.5` |
| [prealgebra_2057](prealgebra_2057.md) | 4 | n | stop | 32699 | 0.017 | `90` | `45` |
| [prealgebra_996](prealgebra_996.md) | 1 | Y | stop | 6928 | 0.0 | `9` | `9` |
| [precalculus_285](precalculus_285.md) | 2 | n | length | 32768 | 0.066 | `6` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 5694 | 0.325 | `(15,-29)` | `(15, -29)` |
| [precalculus_580](precalculus_580.md) | 3 | Y | stop | 12397 | 0.097 | `120^\circ` | `120` |
| [precalculus_807](precalculus_807.md) | 2 | Y | stop | 6789 | 0.132 | `\left( 3, \frac{\pi}{2} \right)` | `(3,\frac{\pi}{2})` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 32768 | 0.12 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 32768 | 0.158 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
| [precalculus_927](precalculus_927.md) | 4 | n | length | 32768 | 0.061 | `90^\circ` | `None` |
| [precalculus_96](precalculus_96.md) | 3 | n | stop | 26053 | 0.168 | `\frac{7}{4}` | `1` |
