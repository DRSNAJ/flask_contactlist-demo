# flask_contactlist-demo
A full stack flask app with a back end database and a react front end.

```
flask_contactlist-demo
├─ .git
│  ├─ COMMIT_EDITMSG
│  ├─ config
│  ├─ description
│  ├─ FETCH_HEAD
│  ├─ HEAD
│  ├─ hooks
│  │  ├─ applypatch-msg.sample
│  │  ├─ commit-msg.sample
│  │  ├─ fsmonitor-watchman.sample
│  │  ├─ post-update.sample
│  │  ├─ pre-applypatch.sample
│  │  ├─ pre-commit.sample
│  │  ├─ pre-merge-commit.sample
│  │  ├─ pre-push.sample
│  │  ├─ pre-rebase.sample
│  │  ├─ pre-receive.sample
│  │  ├─ prepare-commit-msg.sample
│  │  ├─ push-to-checkout.sample
│  │  ├─ sendemail-validate.sample
│  │  └─ update.sample
│  ├─ index
│  ├─ info
│  │  └─ exclude
│  ├─ objects
│  │  ├─ 00
│  │  │  └─ 8b34e16702ee5a0b932fa95cf93d5cccc08d76
│  │  ├─ 01
│  │  │  ├─ 0c80fc9ffc1a9f96939d7b768706eeb20e503a
│  │  │  └─ c9df5c70067bed2ee3da1a9bed61677fce4b9b
│  │  ├─ 04
│  │  │  └─ 48d3d333fcd9515551bdcb9fd89a648ea1e513
│  │  ├─ 05
│  │  │  └─ f6912d99fc9348b6e79258d8417086a8af3254
│  │  ├─ 0c
│  │  │  ├─ 589eccd4d48e270e161a1ab91baee5e5f4b4bc
│  │  │  └─ ae0717e3ff7e55b4bee08ba963429372af9721
│  │  ├─ 0f
│  │  │  ├─ 0d08be02101e74d3b0ae8c4c0f05af48635d38
│  │  │  └─ 5c87be1aaf7f58e0bb1b1eba9167f285adc069
│  │  ├─ 14
│  │  │  └─ 5a088fdcc8d138e92f983ffc59a9e41aeaa0c5
│  │  ├─ 15
│  │  │  └─ 8a46ea43ab5c622ef67ddcc2b7da6a7c483664
│  │  ├─ 17
│  │  │  └─ 2bbcbe5923e425c788872ba57afcf3cff73d02
│  │  ├─ 1a
│  │  │  └─ 286d9dee4e1046cc44f90447d7cc6eb4c3f40a
│  │  ├─ 1e
│  │  │  └─ 10ed92b89400fe84b907d1f19f2f1c09e8acfc
│  │  ├─ 21
│  │  │  └─ a277a78600566d8720b73b4e2c3aad65470258
│  │  ├─ 24
│  │  │  └─ ad7a1dd21e969ac088bbf70738c6e343d67c63
│  │  ├─ 25
│  │  │  └─ 5e4df70d7cb9c4acdad62114128d7666c70565
│  │  ├─ 26
│  │  │  └─ 24c7cb6bb939f40e9f00dc1d3782ac45b7022c
│  │  ├─ 2b
│  │  │  └─ 82057debfc8c2f7dba0c531d7ebae96076bbdb
│  │  ├─ 2c
│  │  │  └─ 9a11c06d51145c29c03f38069b570253ad2b65
│  │  ├─ 2d
│  │  │  └─ f456fa65fb291b38f01a82b49e2770eb74b98c
│  │  ├─ 34
│  │  │  ├─ 6711cca3feac2678a5023fca7b58f8e1c6d498
│  │  │  └─ 85a3a55b7de82faca19c795c854fb66b7c08b4
│  │  ├─ 35
│  │  │  └─ 0b1d334bf8907255b0be8767e45fb086d37f93
│  │  ├─ 36
│  │  │  └─ 1ebe48eb252cd0bbbf1804e3e9f0cfa999fec6
│  │  ├─ 38
│  │  │  ├─ 78e7f53b9a7270b55cb6d6f1b280f2ccd01efa
│  │  │  └─ 8cad14a0218dcccac8ff49e0972c91916a46ad
│  │  ├─ 39
│  │  │  └─ c7fb445f21c0595b52a336b94e5591e22322dc
│  │  ├─ 3d
│  │  │  └─ 432cdf384daf442aec5b0f9e696ebe7541e9ec
│  │  ├─ 3e
│  │  │  └─ 212e1d4307a332e8511f530bc48a4ad5ed6f95
│  │  ├─ 3f
│  │  │  ├─ 737cb4566e17812237fb664d3f53f67e5ff31e
│  │  │  └─ b3548030cb1af96408895fcb6db8d874200b7a
│  │  ├─ 43
│  │  │  └─ edd7579652366bf607f120c8898f959d47eba9
│  │  ├─ 44
│  │  │  └─ ec315d1d63e9856e17aea8eb7452117c97f42f
│  │  ├─ 47
│  │  │  └─ ac42e6556cddd2797031b0cb2d722a5f969202
│  │  ├─ 4b
│  │  │  └─ 4b13eb9232d909cefa0e0db49759a091da79e6
│  │  ├─ 4f
│  │  │  ├─ e933de7c8232ec4c87ff0a0e0f2b2b6fb2b288
│  │  │  └─ f7fe250abccbf5b125d642664fd7ecce89b969
│  │  ├─ 50
│  │  │  └─ bc32650f567fe0af883d5d679f7a392ceada45
│  │  ├─ 51
│  │  │  └─ 253d032d187648e06e1dda594ce1d17cad0cd5
│  │  ├─ 52
│  │  │  ├─ 6a68301f2a96bab45a00d874e86e89280d8300
│  │  │  └─ 972fae97854f1e28da0e271fb82bdd8c8b6abb
│  │  ├─ 53
│  │  │  └─ 6304c2980c66ba82d9bb86ca58903e303926b7
│  │  ├─ 54
│  │  │  ├─ 04cf4e3ac49dc56b12c8a3d519c18126fb7f7f
│  │  │  ├─ 1261a5485b363a072c041f5aa68f711c9aabae
│  │  │  ├─ 7ae0e72f8fda4c386647c979d39902ed81645d
│  │  │  └─ b39dd1d900e866bb91ee441d372a8924b9d87a
│  │  ├─ 55
│  │  │  └─ 7b37c44d5cb352ff331f90e7fba0189cdfa65e
│  │  ├─ 58
│  │  │  └─ cfb4ef3d6bb94b1f0c404c39710fdc410fcff4
│  │  ├─ 5a
│  │  │  └─ 33944a9b41b59a9cf06ee4bb5586c77510f06b
│  │  ├─ 5f
│  │  │  ├─ 36e2d93926962c2e8155545db8407975a456a9
│  │  │  └─ 856f64cad8c451b7c15bd33266c808cf2dad71
│  │  ├─ 61
│  │  │  └─ 19ad9a8faaa5073a454f67b50fb98a25972fd2
│  │  ├─ 68
│  │  │  └─ 345c3a389f92133747f087b2dd94768be3c772
│  │  ├─ 6b
│  │  │  └─ f50e07fd502f77d7320d55e2c9bb24dbedb570
│  │  ├─ 6c
│  │  │  └─ 87de9bb3358469122cc991d5cf578927246184
│  │  ├─ 6d
│  │  │  └─ f958a563dfe243a8d79ca1927a1b7fff4b1d48
│  │  ├─ 6f
│  │  │  └─ ee2d5de4539ecb1b54ddc3bcc7e24a1b54cf68
│  │  ├─ 73
│  │  │  └─ 023e6e778301c55b328d6aba89ddd004012e7e
│  │  ├─ 79
│  │  │  └─ 0099c27711fae4808cbe124f30b4e6a0acb5cd
│  │  ├─ 7a
│  │  │  ├─ 571ba79fcb95e3ec9a45587f7d1a0a8dd884c4
│  │  │  └─ ed31f9cdba6aea9684cb2241e945086525627a
│  │  ├─ 7b
│  │  │  ├─ 146cbf482b91393f9bf5af8075d2ce1e0151b6
│  │  │  ├─ 3f5ff927eb5dc8344c09f6241891baf204b783
│  │  │  └─ a7675f0ea31463778caae10dcae413049a15ce
│  │  ├─ 7c
│  │  │  └─ 271f30c15c75c7973bb4c02dda9a264f9b4ff5
│  │  ├─ 7d
│  │  │  └─ 3b124de55da3114b39d7e0f75df4fa3bbf2c3b
│  │  ├─ 81
│  │  │  └─ 1d850e100c95404668401b569370c28b36dc95
│  │  ├─ 82
│  │  │  └─ a783b130de795c2fe02473bd67c19797c6414a
│  │  ├─ 83
│  │  │  ├─ adfd7fab4ae3e84994eafc319323ec99ebc974
│  │  │  └─ f8b6cf1fb58f07394e0438620a3da1bed32c3a
│  │  ├─ 85
│  │  │  └─ 6ffef83aa2b6ed57c3b9cc9eff1829489bf4d0
│  │  ├─ 91
│  │  │  └─ 6016505c443ccbf2ba5a0080e45c32e7f9e2e4
│  │  ├─ 92
│  │  │  └─ 086439ca446258a7c3ea1745cae5d22d1205b2
│  │  ├─ 94
│  │  │  └─ c0b2fc152a086447a04f62793957235d2475be
│  │  ├─ 95
│  │  │  └─ 0c28e60a38da14e250bc0ee076ff4303eca038
│  │  ├─ 96
│  │  │  ├─ 530866c96e4ad9fa1874e23efceaa251bea41e
│  │  │  └─ affa474b712e8f72f5374567968aa239eb3381
│  │  ├─ 98
│  │  │  ├─ 0e932fd7623ced8e9b8348ea202d57407b4fac
│  │  │  └─ b9a4f60a54bc9ee73a6781a15aeba67bff4fb1
│  │  ├─ 9c
│  │  │  └─ ffd00984486e11d3cb035cf4f02d138ab193f3
│  │  ├─ 9d
│  │  │  └─ 5e1256e7c463cdc1e18497ed51a12e322f9e7d
│  │  ├─ 9e
│  │  │  └─ 1949225c846d4ce118aced772521d16deee379
│  │  ├─ a3
│  │  │  └─ 5c388a16a031098d14c954ccd26fd68f396424
│  │  ├─ a5
│  │  │  └─ 47bf36d8d11a4f89c59c144f24795749086dd1
│  │  ├─ a9
│  │  │  └─ 738abeb8db564c036fce67b4f80193b3143021
│  │  ├─ ab
│  │  │  ├─ 1c7ce953b43834ffa0c6d4a0e2486e60031b73
│  │  │  └─ a2685815049e94e29b561b19b8c6dc779aaadd
│  │  ├─ b4
│  │  │  └─ 6c3586455727115594af6daf4cbfdf0de30fa7
│  │  ├─ b5
│  │  │  ├─ 12c09d476623ff4bf8d0d63c29b784925dbdf8
│  │  │  ├─ 63969354680d8e20a272d17a26107d91725996
│  │  │  └─ dbeaed04a439687f98191a07c4a75269bfa638
│  │  ├─ b7
│  │  │  └─ d30237f81e97978c51236916d6459bbaf27a6c
│  │  ├─ b8
│  │  │  └─ b8473a3696b4f77deff889a84ab45629c42079
│  │  ├─ b9
│  │  │  ├─ 2f3a220807162ebaa8d6eac824857399ecffca
│  │  │  └─ d355df2a5956b526c004531b7b0ffe412461e0
│  │  ├─ ba
│  │  │  └─ 4a2bd072063b51035c3e113ceaa9f5365522fd
│  │  ├─ bb
│  │  │  ├─ 5396bb1d70d7881198a7a693ae0c7faf0dbc16
│  │  │  └─ a9eeaa3d5525a076350502e0b3b6f9cacbf21e
│  │  ├─ bc
│  │  │  ├─ 3d0c5603f7938d338c5f2d93c93ed0368e1ea8
│  │  │  └─ d1a21cdb6751d41077531c9c0c4e2f570e8595
│  │  ├─ bd
│  │  │  ├─ 77271ab060873db26b76537d260e64d974eccd
│  │  │  └─ f89af722b64ef6b01a4ecf6e663bc8ffc42a74
│  │  ├─ be
│  │  │  └─ 2d311445d10782da9aefca45e1d87c4ac6a7b9
│  │  ├─ c0
│  │  │  ├─ 3b4f12383430da8f723cfd559eaffbfde6c354
│  │  │  ├─ 76174808606f491e3bdd878d37da3192662cb2
│  │  │  └─ bfa3219fdd2f20595067c73af7d1779f891de8
│  │  ├─ c1
│  │  │  └─ b81f26ef5d8722cf6595f4f63abdb9ae2c07dd
│  │  ├─ c7
│  │  │  └─ 583c757e99958bc39a71c909fd9eda7722095a
│  │  ├─ c8
│  │  │  ├─ 6d5430386dcd776a366280e648b1a0bd571baa
│  │  │  └─ f5e0ca8da6b272f075d9a10840ef2e2100314f
│  │  ├─ ce
│  │  │  └─ f99ed91263303d35aa6954a8985af3a6efa698
│  │  ├─ d0
│  │  │  └─ ba7a0d2ec6aa724f3ee5fe946ca63e893604ed
│  │  ├─ d3
│  │  │  └─ add314321e13a7041ebb4f22d4234cbf2ce43b
│  │  ├─ d4
│  │  │  └─ 000f49c56fde9b04940577c1ae294fab5ece2f
│  │  ├─ d5
│  │  │  └─ e02b0fc72a7b9188adf39b2804a596df635d86
│  │  ├─ d7
│  │  │  └─ b66b572ed65020f96912a4e1bfca083a312d95
│  │  ├─ df
│  │  │  └─ d80b199be1baec3de08bef6d54f0bf594b7c74
│  │  ├─ e3
│  │  │  └─ 695ce27b9814a4050700882ac688951a6a89ec
│  │  ├─ e4
│  │  │  ├─ 2dee154ee49cc6e8b42739bb0b355f55214999
│  │  │  └─ 6064f7bbd785e86533c453d9b3a44a0ab3a980
│  │  ├─ e6
│  │  │  ├─ 15b3979e13c8b3272c4afda5fbc468a93059af
│  │  │  └─ 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│  │  ├─ e7
│  │  │  ├─ 80d12303b5990ae540263b86e7d2027ffb44a5
│  │  │  └─ b8dfb1b2a60bd50538bec9f876511b9cac21e3
│  │  ├─ eb
│  │  │  └─ 5e10ef5bd6fb8ce0ce51f3a80a6a38ac953b45
│  │  ├─ f3
│  │  │  ├─ 8174a9e428e71cb1fb287ce591bd2b946a8b8a
│  │  │  └─ fe696a6241521b95220b1fcafbbda1758c78b2
│  │  ├─ f4
│  │  │  └─ 778bc78dfb7b0c2d5da03e23132da72453c5bd
│  │  ├─ f7
│  │  │  └─ 68e33fc946e6074d6bd3ce5d454853adb3615e
│  │  ├─ fa
│  │  │  └─ 497c685f7e02ef9edccfc695fb9152b34c8219
│  │  ├─ fc
│  │  │  └─ 2db763763c02a2cef1ac4329df550f149709e3
│  │  ├─ info
│  │  └─ pack
│  │     ├─ pack-9c15b2fc5f9e1b6b9e0bf4cf5b0b3d0d8181dd0c.idx
│  │     ├─ pack-9c15b2fc5f9e1b6b9e0bf4cf5b0b3d0d8181dd0c.pack
│  │     └─ pack-9c15b2fc5f9e1b6b9e0bf4cf5b0b3d0d8181dd0c.rev
│  ├─ ORIG_HEAD
│  ├─ packed-refs
│  └─ refs
│     ├─ heads
│     │  ├─ init_docker_files
│     │  ├─ main
│     │  └─ new_init
│     ├─ remotes
│     │  └─ origin
│     │     ├─ HEAD
│     │     ├─ init_docker_files
│     │     ├─ main
│     │     └─ new_init
│     └─ tags
├─ .gitignore
├─ backend
│  ├─ .dockerignore
│  ├─ config.py
│  ├─ Dockerfile
│  ├─ instance
│  │  └─ database.db
│  ├─ main.py
│  ├─ models.py
│  ├─ requirements.txt
│  ├─ tests
│  │  ├─ .pytest_cache
│  │  │  ├─ .gitignore
│  │  │  ├─ CACHEDIR.TAG
│  │  │  ├─ README.md
│  │  │  └─ v
│  │  │     └─ cache
│  │  │        ├─ lastfailed
│  │  │        ├─ nodeids
│  │  │        └─ stepwise
│  │  ├─ test_add_contact.py
│  │  ├─ test_delete_contacts.py
│  │  ├─ test_display_contacts.py
│  │  ├─ test_update_contact.py
│  │  └─ __init__.py
│  └─ wsgi.py
├─ frontend
│  ├─ .dockerignore
│  ├─ .eslintrc.cjs
│  ├─ .gitignore
│  ├─ build
│  │  ├─ assets
│  │  │  ├─ index-CquO0IcY.js
│  │  │  └─ index-uhysuO_S.css
│  │  └─ index.html
│  ├─ Dockerfile
│  ├─ index.html
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  ├─ README.md
│  ├─ src
│  │  ├─ App.css
│  │  ├─ App.jsx
│  │  ├─ ContactForm.jsx
│  │  ├─ ContactList.jsx
│  │  ├─ index.css
│  │  └─ main.jsx
│  └─ vite.config.js
├─ Jenkinsfile
└─ README.md

```