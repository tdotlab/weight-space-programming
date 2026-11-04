# Run: 2B/math500/A1x3_8k_q8

```json
{
  "name": "A1x3_8k_q8",
  "model": "2B",
  "task": "math500",
  "gguf": "gguf/2B_A1x3-q8_0.gguf",
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
  "acc": 0.42,
  "truncated": 0.58,
  "acc_when_finished": 1.0,
  "n_finished": 42,
  "mean_tokens": 6557,
  "mean_waits_per_kchar": 0.104
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 6037 | 0.118 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 8192 | 0.048 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 1334 | 0.0 | `6+9i` | `6+9i` |
| [algebra_1143](algebra_1143.md) | 5 | n | length | 8192 | 0.183 | `17` | `None` |
| [algebra_1184](algebra_1184.md) | 4 | n | length | 8192 | 0.0 | `129` | `None` |
| [algebra_1255](algebra_1255.md) | 2 | n | length | 8192 | 0.162 | `6` | `None` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 1370 | 0.0 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1275](algebra_1275.md) | 3 | n | length | 8192 | 0.135 | `\frac{\sqrt{3}}{3}` | `None` |
| [algebra_1332](algebra_1332.md) | 3 | Y | stop | 3943 | 0.0 | `9` | `9` |
| [algebra_1339](algebra_1339.md) | 5 | Y | stop | 3054 | 0.132 | `600` | `600` |
| [algebra_170](algebra_170.md) | 3 | Y | stop | 2079 | 0.0 | `11` | `11` |
| [algebra_187](algebra_187.md) | 4 | n | length | 8192 | 0.0 | `3` | `None` |
| [algebra_1934](algebra_1934.md) | 4 | Y | stop | 7290 | 0.0 | `13` | `13` |
| [algebra_2043](algebra_2043.md) | 5 | Y | stop | 4312 | 0.15 | `(-\infty, 2) \cup (3, \infty)` | `(-\infty, 2) \cup (3, \infty)` |
| [algebra_2064](algebra_2064.md) | 5 | Y | stop | 6564 | 0.292 | `81` | `81` |
| [algebra_224](algebra_224.md) | 4 | Y | stop | 3235 | 0.0 | `8` | `8` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 8192 | 0.097 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 8192 | 0.091 | `10` | `None` |
| [algebra_251](algebra_251.md) | 2 | Y | stop | 5864 | 0.113 | `2` | `2` |
| [algebra_2517](algebra_2517.md) | 5 | n | length | 8192 | 0.095 | `-\frac{35}{9}` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | Y | stop | 6921 | 0.208 | `2107` | `2107` |
| [algebra_2593](algebra_2593.md) | 2 | Y | stop | 3206 | 0.0 | `8000` | `8000` |
| [algebra_276](algebra_276.md) | 2 | Y | stop | 7718 | 0.0 | `12` | `12` |
| [algebra_297](algebra_297.md) | 5 | n | length | 8192 | 0.095 | `1736` | `None` |
| [algebra_305](algebra_305.md) | 5 | n | length | 8192 | 0.139 | `5` | `None` |
| [algebra_634](algebra_634.md) | 3 | Y | stop | 4327 | 0.094 | `4` | `4` |
| [algebra_661](algebra_661.md) | 3 | n | length | 8192 | 0.176 | `36` | `None` |
| [algebra_668](algebra_668.md) | 4 | Y | stop | 2012 | 0.0 | `45` | `45` |
| [algebra_694](algebra_694.md) | 3 | Y | stop | 5237 | 0.192 | `16` | `16` |
| [algebra_824](algebra_824.md) | 4 | n | length | 8192 | 0.185 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | Y | stop | 4569 | 0.255 | `2` | `2` |
| [algebra_972](algebra_972.md) | 4 | Y | stop | 7256 | 0.123 | `\frac{11}{2}` | `\frac{11}{2}` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 8192 | 0.044 | `\frac{11}{36}` | `1` |
| [counting_and_probability_134](counting_and_probability_134.md) | 4 | n | length | 8192 | 0.031 | `720` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 1834 | 0.0 | `6` | `6` |
| [counting_and_probability_199](counting_and_probability_199.md) | 2 | n | length | 8192 | 0.0 | `13` | `None` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 1834 | 0.0 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 7990 | 0.065 | `28` | `28` |
| [counting_and_probability_71](counting_and_probability_71.md) | 3 | n | length | 8192 | 0.0 | `3` | `None` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 8192 | 0.0 | `\frac{1}{4}` | `None` |
| [geometry_106](geometry_106.md) | 2 | n | length | 8192 | 0.036 | `31` | `None` |
| [geometry_347](geometry_347.md) | 3 | Y | stop | 6608 | 0.355 | `76^\circ` | `76` |
| [geometry_456](geometry_456.md) | 2 | n | length | 8192 | 0.071 | `3` | `None` |
| [geometry_547](geometry_547.md) | 4 | n | length | 8192 | 0.128 | `54` | `None` |
| [geometry_627](geometry_627.md) | 4 | n | length | 8192 | 0.235 | `17` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 8192 | 0.166 | `1+2\sqrt{3}` | `None` |
| [geometry_802](geometry_802.md) | 2 | Y | stop | 6816 | 0.449 | `12` | `12` |
| [geometry_880](geometry_880.md) | 5 | n | length | 8192 | 0.0 | `2\sqrt{113}` | `None` |
| [geometry_947](geometry_947.md) | 5 | n | length | 8192 | 0.0 | `-\frac{24}{25}` | `None` |
| [geometry_967](geometry_967.md) | 3 | n | length | 8192 | 0.0 | `72` | `None` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 8192 | 0.2 | `-2,1` | `None` |
| [intermediate_algebra_117](intermediate_algebra_117.md) | 5 | n | length | 8192 | 0.254 | `15` | `None` |
| [intermediate_algebra_1217](intermediate_algebra_1217.md) | 2 | n | length | 8192 | 0.262 | `x^5 - x^4 + x^3 - x^2 + x - 1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 8192 | 0.239 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1365](intermediate_algebra_1365.md) | 3 | n | length | 8192 | 0.0 | `15` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 8192 | 0.093 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 8192 | 0.11 | `331` | `None` |
| [intermediate_algebra_1510](intermediate_algebra_1510.md) | 5 | n | length | 8192 | 0.383 | `0` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 8192 | 0.209 | `27648` | `None` |
| [intermediate_algebra_1714](intermediate_algebra_1714.md) | 1 | Y | stop | 3200 | 0.0 | `(5,\infty)` | `(5, \infty)` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 8192 | 0.166 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 8192 | 0.53 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_2015](intermediate_algebra_2015.md) | 5 | n | length | 8192 | 0.259 | `\{1\pm\sqrt{5},-2\}` | `None` |
| [intermediate_algebra_2146](intermediate_algebra_2146.md) | 4 | n | length | 8192 | 0.051 | `406` | `None` |
| [intermediate_algebra_362](intermediate_algebra_362.md) | 4 | n | length | 8192 | 0.193 | `40` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 8192 | 0.048 | `9` | `y > 0 and y \neq 1` |
| [intermediate_algebra_960](intermediate_algebra_960.md) | 5 | n | length | 8192 | 0.083 | `\frac{17}{21}` | `None` |
| [number_theory_1002](number_theory_1002.md) | 5 | n | length | 8192 | 0.056 | `1440` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 8192 | 0.033 | `203` | `None` |
| [number_theory_1287](number_theory_1287.md) | 4 | n | length | 8192 | 0.078 | `8` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 8192 | 0.213 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 8192 | 0.0 | `1030` | `None` |
| [number_theory_686](number_theory_686.md) | 2 | Y | stop | 5397 | 0.265 | `4` | `4` |
| [number_theory_691](number_theory_691.md) | 3 | Y | stop | 4870 | 0.129 | `255` | `255` |
| [number_theory_72](number_theory_72.md) | 4 | Y | stop | 3632 | 0.0 | `121` | `121` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 8192 | 0.0 | `6` | `None` |
| [number_theory_931](number_theory_931.md) | 2 | n | length | 8192 | 0.094 | `49` | `None` |
| [prealgebra_1003](prealgebra_1003.md) | 5 | n | length | 8192 | 0.035 | `\frac{270}7\text{ degrees}` | `None` |
| [prealgebra_105](prealgebra_105.md) | 1 | n | length | 8192 | 0.034 | `\text{east}` | `None` |
| [prealgebra_1114](prealgebra_1114.md) | 2 | n | length | 8192 | 0.04 | `15\mbox{ cm}^2` | `None` |
| [prealgebra_1203](prealgebra_1203.md) | 5 | Y | stop | 4818 | 0.321 | `\$36` | `36` |
| [prealgebra_1227](prealgebra_1227.md) | 3 | Y | stop | 7130 | 0.0 | `60` | `60` |
| [prealgebra_1238](prealgebra_1238.md) | 3 | Y | stop | 5138 | 0.0 | `2` | `2` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | Y | stop | 4616 | 0.0 | `8` | `8` |
| [prealgebra_1302](prealgebra_1302.md) | 4 | Y | stop | 1805 | 0.0 | `11\sqrt2` | `11\sqrt{2}` |
| [prealgebra_1423](prealgebra_1423.md) | 5 | Y | stop | 3561 | 0.0 | `12\pi` | `12\pi` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | Y | stop | 3205 | 0.0 | `4` | `4` |
| [prealgebra_1742](prealgebra_1742.md) | 3 | Y | stop | 2117 | 0.0 | `\dfrac{33}{100}` | `\frac{33}{100}` |
| [prealgebra_1807](prealgebra_1807.md) | 3 | Y | stop | 7326 | 0.045 | `120` | `120` |
| [prealgebra_2019](prealgebra_2019.md) | 2 | Y | stop | 1449 | 0.0 | `4.5` | `4.5` |
| [prealgebra_2057](prealgebra_2057.md) | 4 | Y | stop | 2438 | 0.0 | `90` | `90` |
| [prealgebra_996](prealgebra_996.md) | 1 | Y | stop | 2149 | 0.0 | `9` | `9` |
| [precalculus_285](precalculus_285.md) | 2 | n | length | 8192 | 0.0 | `6` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 1818 | 0.435 | `(15,-29)` | `(15, -29)` |
| [precalculus_580](precalculus_580.md) | 3 | n | length | 8192 | 0.166 | `120^\circ` | `A - B` |
| [precalculus_807](precalculus_807.md) | 2 | Y | stop | 4484 | 0.156 | `\left( 3, \frac{\pi}{2} \right)` | `(3, \frac{\pi}{2})` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 8192 | 0.054 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 8192 | 0.165 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
| [precalculus_927](precalculus_927.md) | 4 | n | length | 8192 | 0.09 | `90^\circ` | `None` |
| [precalculus_96](precalculus_96.md) | 3 | n | length | 8192 | 0.217 | `\frac{7}{4}` | `None` |
