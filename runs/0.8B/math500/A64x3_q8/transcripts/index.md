# Run: 0.8B/math500/A64x3_q8

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
  "n": 100,
  "max_tokens": 16384,
  "think": true,
  "seed": 0,
  "first": 0,
  "backend_sampling": true,
  "acc": 0.3,
  "truncated": 0.7,
  "acc_when_finished": 1.0,
  "n_finished": 30,
  "mean_tokens": 14019,
  "mean_waits_per_kchar": 0.108
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 15618 | 0.237 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 16384 | 0.162 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 6200 | 0.05 | `6+9i` | `6+9i` |
| [algebra_1143](algebra_1143.md) | 5 | n | length | 16384 | 0.101 | `17` | `None` |
| [algebra_1184](algebra_1184.md) | 4 | n | length | 16384 | 0.0 | `129` | `None` |
| [algebra_1255](algebra_1255.md) | 2 | Y | stop | 4374 | 0.076 | `6` | `6` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 15810 | 0.058 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1275](algebra_1275.md) | 3 | n | length | 16384 | 0.11 | `\frac{\sqrt{3}}{3}` | `None` |
| [algebra_1332](algebra_1332.md) | 3 | Y | stop | 9835 | 0.065 | `9` | `9` |
| [algebra_1339](algebra_1339.md) | 5 | Y | stop | 10432 | 0.103 | `600` | `600` |
| [algebra_170](algebra_170.md) | 3 | Y | stop | 7455 | 0.053 | `11` | `11` |
| [algebra_187](algebra_187.md) | 4 | Y | stop | 12811 | 0.147 | `3` | `3` |
| [algebra_1934](algebra_1934.md) | 4 | n | length | 16384 | 0.038 | `13` | `None` |
| [algebra_2043](algebra_2043.md) | 5 | n | length | 16384 | 0.04 | `(-\infty, 2) \cup (3, \infty)` | `None` |
| [algebra_2064](algebra_2064.md) | 5 | n | length | 16384 | 0.075 | `81` | `None` |
| [algebra_224](algebra_224.md) | 4 | n | length | 16384 | 0.247 | `8` | `None` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 16384 | 0.157 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | Y | stop | 8612 | 0.158 | `10` | `10` |
| [algebra_251](algebra_251.md) | 2 | Y | stop | 7733 | 0.171 | `2` | `2` |
| [algebra_2517](algebra_2517.md) | 5 | n | length | 16384 | 0.082 | `-\frac{35}{9}` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 16384 | 0.098 | `2107` | `None` |
| [algebra_2593](algebra_2593.md) | 2 | Y | stop | 10194 | 0.21 | `8000` | `8000` |
| [algebra_276](algebra_276.md) | 2 | n | length | 16384 | 0.156 | `12` | `None` |
| [algebra_297](algebra_297.md) | 5 | n | length | 16384 | 0.169 | `1736` | `None` |
| [algebra_305](algebra_305.md) | 5 | Y | stop | 4875 | 0.069 | `5` | `5` |
| [algebra_634](algebra_634.md) | 3 | n | length | 16384 | 0.026 | `4` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | length | 16384 | 0.069 | `36` | `None` |
| [algebra_668](algebra_668.md) | 4 | Y | stop | 11240 | 0.028 | `45` | `45` |
| [algebra_694](algebra_694.md) | 3 | n | length | 16384 | 0.022 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 16384 | 0.075 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | n | length | 16384 | 0.053 | `2` | `None` |
| [algebra_972](algebra_972.md) | 4 | n | length | 16384 | 0.156 | `\frac{11}{2}` | `None` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 16384 | 0.045 | `\frac{11}{36}` | `None` |
| [counting_and_probability_134](counting_and_probability_134.md) | 4 | n | length | 16384 | 0.16 | `720` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 5255 | 0.108 | `6` | `6` |
| [counting_and_probability_199](counting_and_probability_199.md) | 2 | n | length | 16384 | 0.088 | `13` | `None` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 5029 | 0.065 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 8458 | 0.031 | `28` | `28` |
| [counting_and_probability_71](counting_and_probability_71.md) | 3 | n | length | 16384 | 0.099 | `3` | `None` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 16384 | 0.083 | `\frac{1}{4}` | `None` |
| [geometry_106](geometry_106.md) | 2 | Y | stop | 2485 | 0.128 | `31` | `31` |
| [geometry_347](geometry_347.md) | 3 | Y | stop | 3349 | 0.088 | `76^\circ` | `76` |
| [geometry_456](geometry_456.md) | 2 | Y | stop | 12667 | 0.098 | `3` | `3` |
| [geometry_547](geometry_547.md) | 4 | n | length | 16384 | 0.119 | `54` | `None` |
| [geometry_627](geometry_627.md) | 4 | n | length | 16384 | 0.08 | `17` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 16384 | 0.118 | `1+2\sqrt{3}` | `None` |
| [geometry_802](geometry_802.md) | 2 | Y | stop | 6821 | 0.049 | `12` | `12` |
| [geometry_880](geometry_880.md) | 5 | n | length | 16384 | 0.064 | `2\sqrt{113}` | `None` |
| [geometry_947](geometry_947.md) | 5 | n | length | 16384 | 0.02 | `-\frac{24}{25}` | `None` |
| [geometry_967](geometry_967.md) | 3 | Y | stop | 11693 | 0.047 | `72` | `72` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 16384 | 0.304 | `-2,1` | `None` |
| [intermediate_algebra_117](intermediate_algebra_117.md) | 5 | n | length | 16384 | 0.14 | `15` | `None` |
| [intermediate_algebra_1217](intermediate_algebra_1217.md) | 2 | n | length | 16384 | 0.195 | `x^5 - x^4 + x^3 - x^2 + x - 1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 16384 | 0.168 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1365](intermediate_algebra_1365.md) | 3 | n | length | 16384 | 0.0 | `15` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 16384 | 0.061 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 16384 | 0.027 | `331` | `None` |
| [intermediate_algebra_1510](intermediate_algebra_1510.md) | 5 | n | length | 16384 | 0.39 | `0` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 16384 | 0.167 | `27648` | `None` |
| [intermediate_algebra_1714](intermediate_algebra_1714.md) | 1 | Y | stop | 3685 | 0.08 | `(5,\infty)` | `(5, \infty)` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 16384 | 0.133 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 16384 | 0.356 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_2015](intermediate_algebra_2015.md) | 5 | n | length | 16384 | 0.394 | `\{1\pm\sqrt{5},-2\}` | `None` |
| [intermediate_algebra_2146](intermediate_algebra_2146.md) | 4 | n | length | 16384 | 0.109 | `406` | `None` |
| [intermediate_algebra_362](intermediate_algebra_362.md) | 4 | n | length | 16384 | 0.055 | `40` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | Y | stop | 15916 | 0.079 | `9` | `9` |
| [intermediate_algebra_960](intermediate_algebra_960.md) | 5 | n | length | 16384 | 0.268 | `\frac{17}{21}` | `None` |
| [number_theory_1002](number_theory_1002.md) | 5 | n | length | 16384 | 0.083 | `1440` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 16384 | 0.035 | `203` | `None` |
| [number_theory_1287](number_theory_1287.md) | 4 | n | length | 16384 | 0.207 | `8` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 16384 | 0.374 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 16384 | 0.251 | `1030` | `None` |
| [number_theory_686](number_theory_686.md) | 2 | n | length | 16384 | 0.109 | `4` | `None` |
| [number_theory_691](number_theory_691.md) | 3 | n | length | 16384 | 0.053 | `255` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | n | length | 16384 | 0.034 | `121` | `None` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 16384 | 0.118 | `6` | `None` |
| [number_theory_931](number_theory_931.md) | 2 | n | length | 16384 | 0.086 | `49` | `None` |
| [prealgebra_1003](prealgebra_1003.md) | 5 | n | length | 16384 | 0.019 | `\frac{270}7\text{ degrees}` | `None` |
| [prealgebra_105](prealgebra_105.md) | 1 | n | length | 16384 | 0.054 | `\text{east}` | `None` |
| [prealgebra_1114](prealgebra_1114.md) | 2 | n | length | 16384 | 0.02 | `15\mbox{ cm}^2` | `0` |
| [prealgebra_1203](prealgebra_1203.md) | 5 | n | length | 16384 | 0.057 | `\$36` | `None` |
| [prealgebra_1227](prealgebra_1227.md) | 3 | n | length | 16384 | 0.035 | `60` | `None` |
| [prealgebra_1238](prealgebra_1238.md) | 3 | Y | stop | 13048 | 0.327 | `2` | `2` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 16384 | 0.077 | `8` | `None` |
| [prealgebra_1302](prealgebra_1302.md) | 4 | Y | stop | 3336 | 0.212 | `11\sqrt2` | `11\sqrt{2}` |
| [prealgebra_1423](prealgebra_1423.md) | 5 | n | length | 16384 | 0.052 | `12\pi` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 16384 | 0.0 | `4` | `None` |
| [prealgebra_1742](prealgebra_1742.md) | 3 | n | length | 16384 | 0.04 | `\dfrac{33}{100}` | `None` |
| [prealgebra_1807](prealgebra_1807.md) | 3 | n | length | 16384 | 0.039 | `120` | `None` |
| [prealgebra_2019](prealgebra_2019.md) | 2 | Y | stop | 8667 | 0.111 | `4.5` | `4.5` |
| [prealgebra_2057](prealgebra_2057.md) | 4 | n | length | 16384 | 0.015 | `90` | `None` |
| [prealgebra_996](prealgebra_996.md) | 1 | Y | stop | 6540 | 0.102 | `9` | `9` |
| [precalculus_285](precalculus_285.md) | 2 | n | length | 16384 | 0.243 | `6` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 2093 | 0.0 | `(15,-29)` | `(15, -29)` |
| [precalculus_580](precalculus_580.md) | 3 | Y | stop | 14070 | 0.122 | `120^\circ` | `120^\circ` |
| [precalculus_807](precalculus_807.md) | 2 | Y | stop | 6678 | 0.046 | `\left( 3, \frac{\pi}{2} \right)` | `(3, \frac{\pi}{2})` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 16384 | 0.027 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 16384 | 0.115 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
| [precalculus_927](precalculus_927.md) | 4 | n | length | 16384 | 0.073 | `90^\circ` | `None` |
| [precalculus_96](precalculus_96.md) | 3 | n | length | 16384 | 0.036 | `\frac{7}{4}` | `None` |
