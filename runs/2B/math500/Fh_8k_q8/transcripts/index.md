# Run: 2B/math500/Fh_8k_q8

```json
{
  "name": "Fh_8k_q8",
  "model": "2B",
  "task": "math500",
  "gguf": "gguf/2B_Fh-q8_0.gguf",
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
  "acc": 0.22,
  "truncated": 0.78,
  "acc_when_finished": 1.0,
  "n_finished": 22,
  "mean_tokens": 7329,
  "mean_waits_per_kchar": 1.603
}
```

| problem | level | correct | finish | tokens | waits/kchar | gold | pred |
|---|---|---|---|---|---|---|---|
| [algebra_1031](algebra_1031.md) | 5 | Y | stop | 6240 | 1.002 | `\frac{11}{2}` | `5.5` |
| [algebra_1082](algebra_1082.md) | 4 | n | length | 8192 | 1.891 | `23` | `None` |
| [algebra_1098](algebra_1098.md) | 3 | Y | stop | 5391 | 0.714 | `6+9i` | `6+9i` |
| [algebra_1143](algebra_1143.md) | 5 | n | length | 8192 | 2.131 | `17` | `None` |
| [algebra_1184](algebra_1184.md) | 4 | n | length | 8192 | 1.194 | `129` | `None` |
| [algebra_1255](algebra_1255.md) | 2 | n | length | 8192 | 2.16 | `6` | `None` |
| [algebra_1265](algebra_1265.md) | 2 | Y | stop | 6765 | 0.528 | `\frac{3}{2}` | `\frac{3}{2}` |
| [algebra_1275](algebra_1275.md) | 3 | n | length | 8192 | 2.569 | `\frac{\sqrt{3}}{3}` | `None` |
| [algebra_1332](algebra_1332.md) | 3 | Y | stop | 6183 | 0.907 | `9` | `9` |
| [algebra_1339](algebra_1339.md) | 5 | n | length | 8192 | 1.784 | `600` | `None` |
| [algebra_170](algebra_170.md) | 3 | n | length | 8192 | 2.302 | `11` | `None` |
| [algebra_187](algebra_187.md) | 4 | n | length | 8192 | 1.73 | `3` | `None` |
| [algebra_1934](algebra_1934.md) | 4 | n | length | 8192 | 1.897 | `13` | `None` |
| [algebra_2043](algebra_2043.md) | 5 | n | length | 8192 | 1.42 | `(-\infty, 2) \cup (3, \infty)` | `None` |
| [algebra_2064](algebra_2064.md) | 5 | n | length | 8192 | 1.912 | `81` | `None` |
| [algebra_224](algebra_224.md) | 4 | Y | stop | 2650 | 0.398 | `8` | `8` |
| [algebra_2264](algebra_2264.md) | 5 | n | length | 8192 | 1.945 | `1+2i` | `None` |
| [algebra_2391](algebra_2391.md) | 4 | n | length | 8192 | 1.374 | `10` | `None` |
| [algebra_251](algebra_251.md) | 2 | Y | stop | 2802 | 0.752 | `2` | `2` |
| [algebra_2517](algebra_2517.md) | 5 | n | length | 8192 | 2.957 | `-\frac{35}{9}` | `None` |
| [algebra_2570](algebra_2570.md) | 4 | n | length | 8192 | 4.094 | `2107` | `None` |
| [algebra_2593](algebra_2593.md) | 2 | n | length | 8192 | 1.628 | `8000` | `None` |
| [algebra_276](algebra_276.md) | 2 | n | length | 8192 | 1.624 | `12` | `None` |
| [algebra_297](algebra_297.md) | 5 | n | length | 8192 | 2.107 | `1736` | `None` |
| [algebra_305](algebra_305.md) | 5 | n | length | 8192 | 1.38 | `5` | `None` |
| [algebra_634](algebra_634.md) | 3 | n | length | 8192 | 1.585 | `4` | `None` |
| [algebra_661](algebra_661.md) | 3 | n | length | 8192 | 1.74 | `36` | `None` |
| [algebra_668](algebra_668.md) | 4 | Y | stop | 1916 | 0.372 | `45` | `45` |
| [algebra_694](algebra_694.md) | 3 | n | length | 8192 | 1.187 | `16` | `None` |
| [algebra_824](algebra_824.md) | 4 | n | length | 8192 | 1.805 | `12` | `None` |
| [algebra_907](algebra_907.md) | 4 | n | length | 8192 | 2.115 | `2` | `None` |
| [algebra_972](algebra_972.md) | 4 | n | length | 8192 | 1.073 | `\frac{11}{2}` | `None` |
| [counting_and_probability_1114](counting_and_probability_1114.md) | 4 | n | length | 8192 | 1.249 | `\frac{11}{36}` | `None` |
| [counting_and_probability_134](counting_and_probability_134.md) | 4 | n | length | 8192 | 1.522 | `720` | `None` |
| [counting_and_probability_190](counting_and_probability_190.md) | 2 | Y | stop | 3259 | 0.281 | `6` | `6` |
| [counting_and_probability_199](counting_and_probability_199.md) | 2 | n | length | 8192 | 1.404 | `13` | `None` |
| [counting_and_probability_23957](counting_and_probability_23957.md) | 3 | Y | stop | 4411 | 0.848 | `210` | `210` |
| [counting_and_probability_389](counting_and_probability_389.md) | 2 | Y | stop | 2066 | 0.27 | `28` | `28` |
| [counting_and_probability_71](counting_and_probability_71.md) | 3 | n | length | 8192 | 1.209 | `3` | `None` |
| [counting_and_probability_803](counting_and_probability_803.md) | 4 | n | length | 8192 | 1.024 | `\frac{1}{4}` | `None` |
| [geometry_106](geometry_106.md) | 2 | Y | stop | 6354 | 0.87 | `31` | `31` |
| [geometry_347](geometry_347.md) | 3 | n | length | 8192 | 1.926 | `76^\circ` | `None` |
| [geometry_456](geometry_456.md) | 2 | n | length | 8192 | 1.694 | `3` | `None` |
| [geometry_547](geometry_547.md) | 4 | n | length | 8192 | 1.933 | `54` | `None` |
| [geometry_627](geometry_627.md) | 4 | n | length | 8192 | 1.104 | `17` | `None` |
| [geometry_711](geometry_711.md) | 5 | n | length | 8192 | 1.942 | `1+2\sqrt{3}` | `None` |
| [geometry_802](geometry_802.md) | 2 | Y | stop | 4208 | 0.956 | `12` | `12` |
| [geometry_880](geometry_880.md) | 5 | n | length | 8192 | 1.144 | `2\sqrt{113}` | `None` |
| [geometry_947](geometry_947.md) | 5 | n | length | 8192 | 1.434 | `-\frac{24}{25}` | `None` |
| [geometry_967](geometry_967.md) | 3 | n | length | 8192 | 1.828 | `72` | `None` |
| [intermediate_algebra_1102](intermediate_algebra_1102.md) | 1 | n | length | 8192 | 2.087 | `-2,1` | `None` |
| [intermediate_algebra_117](intermediate_algebra_117.md) | 5 | n | length | 8192 | 2.934 | `15` | `None` |
| [intermediate_algebra_1217](intermediate_algebra_1217.md) | 2 | n | length | 8192 | 2.597 | `x^5 - x^4 + x^3 - x^2 + x - 1` | `None` |
| [intermediate_algebra_1279](intermediate_algebra_1279.md) | 5 | n | length | 8192 | 2.506 | `\frac{2}{1005}` | `None` |
| [intermediate_algebra_1365](intermediate_algebra_1365.md) | 3 | n | length | 8192 | 2.177 | `15` | `None` |
| [intermediate_algebra_1405](intermediate_algebra_1405.md) | 4 | n | length | 8192 | 1.81 | `16 \sqrt{3}` | `None` |
| [intermediate_algebra_1462](intermediate_algebra_1462.md) | 5 | n | length | 8192 | 2.164 | `331` | `None` |
| [intermediate_algebra_1510](intermediate_algebra_1510.md) | 5 | n | length | 8192 | 2.983 | `0` | `None` |
| [intermediate_algebra_158](intermediate_algebra_158.md) | 5 | n | length | 8192 | 2.152 | `27648` | `None` |
| [intermediate_algebra_1714](intermediate_algebra_1714.md) | 1 | Y | stop | 2467 | 0.477 | `(5,\infty)` | `(5, \infty)` |
| [intermediate_algebra_1797](intermediate_algebra_1797.md) | 4 | n | length | 8192 | 2.778 | `2 \sqrt{5}` | `None` |
| [intermediate_algebra_1806](intermediate_algebra_1806.md) | 5 | n | length | 8192 | 2.137 | `\frac{13}{4}` | `None` |
| [intermediate_algebra_2015](intermediate_algebra_2015.md) | 5 | n | length | 8192 | 2.676 | `\{1\pm\sqrt{5},-2\}` | `None` |
| [intermediate_algebra_2146](intermediate_algebra_2146.md) | 4 | n | length | 8192 | 2.96 | `406` | `None` |
| [intermediate_algebra_362](intermediate_algebra_362.md) | 4 | n | length | 8192 | 2.083 | `40` | `None` |
| [intermediate_algebra_834](intermediate_algebra_834.md) | 3 | n | length | 8192 | 1.441 | `9` | `None` |
| [intermediate_algebra_960](intermediate_algebra_960.md) | 5 | n | length | 8192 | 2.105 | `\frac{17}{21}` | `None` |
| [number_theory_1002](number_theory_1002.md) | 5 | n | length | 8192 | 1.989 | `1440` | `None` |
| [number_theory_1055](number_theory_1055.md) | 5 | n | length | 8192 | 1.323 | `203` | `None` |
| [number_theory_1287](number_theory_1287.md) | 4 | n | length | 8192 | 0.81 | `8` | `None` |
| [number_theory_516](number_theory_516.md) | 4 | n | length | 8192 | 2.598 | `2516_8` | `None` |
| [number_theory_533](number_theory_533.md) | 4 | n | length | 8192 | 2.305 | `1030` | `None` |
| [number_theory_686](number_theory_686.md) | 2 | n | length | 8192 | 2.529 | `4` | `None` |
| [number_theory_691](number_theory_691.md) | 3 | n | length | 8192 | 1.7 | `255` | `None` |
| [number_theory_72](number_theory_72.md) | 4 | Y | stop | 5185 | 0.928 | `121` | `121` |
| [number_theory_838](number_theory_838.md) | 5 | n | length | 8192 | 2.06 | `6` | `None` |
| [number_theory_931](number_theory_931.md) | 2 | n | length | 8192 | 1.759 | `49` | `None` |
| [prealgebra_1003](prealgebra_1003.md) | 5 | n | length | 8192 | 2.076 | `\frac{270}7\text{ degrees}` | `None` |
| [prealgebra_105](prealgebra_105.md) | 1 | n | length | 8192 | 0.918 | `\text{east}` | `None` |
| [prealgebra_1114](prealgebra_1114.md) | 2 | n | length | 8192 | 1.776 | `15\mbox{ cm}^2` | `None` |
| [prealgebra_1203](prealgebra_1203.md) | 5 | n | length | 8192 | 1.004 | `\$36` | `None` |
| [prealgebra_1227](prealgebra_1227.md) | 3 | n | length | 8192 | 0.597 | `60` | `None` |
| [prealgebra_1238](prealgebra_1238.md) | 3 | Y | stop | 6909 | 1.023 | `2` | `2` |
| [prealgebra_1251](prealgebra_1251.md) | 5 | n | length | 8192 | 1.965 | `8` | `None` |
| [prealgebra_1302](prealgebra_1302.md) | 4 | Y | stop | 1580 | 0.226 | `11\sqrt2` | `11\sqrt{2}` |
| [prealgebra_1423](prealgebra_1423.md) | 5 | n | length | 8192 | 1.099 | `12\pi` | `None` |
| [prealgebra_1686](prealgebra_1686.md) | 3 | n | length | 8192 | 1.417 | `4` | `None` |
| [prealgebra_1742](prealgebra_1742.md) | 3 | Y | stop | 5699 | 1.043 | `\dfrac{33}{100}` | `\frac{33}{100}` |
| [prealgebra_1807](prealgebra_1807.md) | 3 | n | length | 8192 | 0.858 | `120` | `None` |
| [prealgebra_2019](prealgebra_2019.md) | 2 | Y | stop | 1221 | 0.0 | `4.5` | `4.5` |
| [prealgebra_2057](prealgebra_2057.md) | 4 | Y | stop | 7616 | 0.988 | `90` | `90` |
| [prealgebra_996](prealgebra_996.md) | 1 | Y | stop | 4027 | 1.055 | `9` | `9` |
| [precalculus_285](precalculus_285.md) | 2 | n | length | 8192 | 2.422 | `6` | `None` |
| [precalculus_43](precalculus_43.md) | 1 | Y | stop | 887 | 0.0 | `(15,-29)` | `(15, -29)` |
| [precalculus_580](precalculus_580.md) | 3 | n | length | 8192 | 1.917 | `120^\circ` | `None` |
| [precalculus_807](precalculus_807.md) | 2 | Y | stop | 6067 | 0.375 | `\left( 3, \frac{\pi}{2} \right)` | `(3, \frac{\pi}{2})` |
| [precalculus_881](precalculus_881.md) | 4 | n | length | 8192 | 1.488 | `\begin{pmatrix} -18 \\ -49 \\ 96 \end{pmatrix}` | `None` |
| [precalculus_920](precalculus_920.md) | 4 | n | length | 8192 | 2.777 | `\begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix}` | `None` |
| [precalculus_927](precalculus_927.md) | 4 | n | length | 8192 | 2.256 | `90^\circ` | `None` |
| [precalculus_96](precalculus_96.md) | 3 | n | length | 8192 | 2.052 | `\frac{7}{4}` | `None` |
