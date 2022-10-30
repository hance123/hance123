# -*- coding = utf-8 -*-#
# @Time : 2022/7/14 16:10
# @authore : admin
# @File : 自动化dbd.py
# @software: PyCharm
import random
import  numpy as np
import time
import requests
import re
import jsonpath
import json
import datetime
import cookie3
import xlrd
import pyttsx3
#listcookie,one wxh,two,zmt,three,msl,four,pqs
#提醒列表为wxh账号提供
cookie_list=[
'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; __jdv=116764038|direct|-|none|-|1664081577279; _s_id=mkbjh7luratv5s3hdff1664203922979cctz; logining=1; mkbjh7luratv5s3hdff1664203922979cctz=683; wlfstk_smdl=xbjqbk6w5n985smkhy3b34nsdpn5h55e; TrackID=1N1Z9FbOGQK6ZvCN5ZRFtLVmuA9grGD0cA4ygwJU5I7rzYIJURK9E71EPVocfq1L3fOLKgPYV76ZGTOb9zJ6dGVuvIMx1IwKEuwxPxtDwJrc; thor=5F786C19055EA6D4528320CFE3AFBBE289FD74E2CBE56D51EAE8BB6A17EB1171E600BEAE95E9131B166EFD7452A6F79ACD195BCA4F683007D2FEAE8601CFC89220CC90875ABD41523421A40468346D96BEA1C604A496418ED88C2FFF14D78417472269AAFE56EDD7EABF6FF754A56894D5F3C6F2F26A87AEF98E5BACE4493194338533781AFB3E1F0DA3BCAE5E8C74D52462F5FE34C6D77E4854827DCB089925; pinId=mfhWuZ6YEOjhTrDqbvPA9bV9-x-f3wj7; pin=jd_6ceba11981d73; unick=j77jshumkdhh; ceshi3.com=201; _tp=BbZ7YJ%2BLlkswBnre%2F3PJjpczJvkNYIWKVCjfCuVa8JU%3D; _pst=jd_6ceba11981d73; __jda=116764038.1421839581.1652269721.1664467253.1664501687.286; __jdb=116764038.7.1421839581|286.1664501687; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; __jdv=116764038|direct|-|none|-|1664081577279; _s_id=mkbjh7luratv5s3hdff1664203922979cctz; logining=1; mkbjh7luratv5s3hdff1664203922979cctz=683; wlfstk_smdl=xbjqbk6w5n985smkhy3b34nsdpn5h55e; TrackID=1N1Z9FbOGQK6ZvCN5ZRFtLVmuA9grGD0cA4ygwJU5I7rzYIJURK9E71EPVocfq1L3fOLKgPYV76ZGTOb9zJ6dGVuvIMx1IwKEuwxPxtDwJrc; thor=5F786C19055EA6D4528320CFE3AFBBE289FD74E2CBE56D51EAE8BB6A17EB1171E600BEAE95E9131B166EFD7452A6F79ACD195BCA4F683007D2FEAE8601CFC89220CC90875ABD41523421A40468346D96BEA1C604A496418ED88C2FFF14D78417472269AAFE56EDD7EABF6FF754A56894D5F3C6F2F26A87AEF98E5BACE4493194338533781AFB3E1F0DA3BCAE5E8C74D52462F5FE34C6D77E4854827DCB089925; pinId=mfhWuZ6YEOjhTrDqbvPA9bV9-x-f3wj7; pin=jd_6ceba11981d73; unick=j77jshumkdhh; ceshi3.com=201; _tp=BbZ7YJ%2BLlkswBnre%2F3PJjpczJvkNYIWKVCjfCuVa8JU%3D; _pst=jd_6ceba11981d73; __jda=116764038.1421839581.1652269721.1664467253.1664501687.286; __jdb=116764038.7.1421839581|286.1664501687; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
# ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; areaId=4; ipLoc-djd=4-51026-58458-0; _s_id=gbn10972fc6ac4byqe61663806970020uq5c; logining=1; __jdv=116764038|direct|-|none|-|1664081577279; gbn10972fc6ac4byqe61663806970020uq5c=193; wlfstk_smdl=97i7rdgwvlxfbr9ftjsgk3wzc05z8msh; TrackID=1ykuvWgl0ly6BlXRWm0FVa8-8wOboW6c4vQ9yzCE3vEQnlVHYbtdERycAumSIt7E_SKjqYhqWQdye2j_Q0LeyvQkIy5HkD9GHtMJvTojAnsM; thor=6D375518B286DCBB9C151E4BA8D59FE82B4D91988513FFF099F2F370B9EDA78F98CC034BA8EE7CCA134643A9D59C093ADC32F7CB81551057ECF95E8850D1CABA5D965EC265DFFF668EDC64D2CB0DEF7CA0C309E48E10B498799CB38663A8E772AAED21B85FA75C705989235C89B883E77C7BE0AEC8F9833418BB998362A804B42186A701F762F7C5EABB46C5C17D826F77A692472601B33C15DA79E933C271EA; pinId=uopmnhDtONwh-ZOCvyZcLrV9-x-f3wj7; pin=jd_4ee26156e156b; unick=sjnszmtone; ceshi3.com=103; _tp=M0evnQ3Uww7FuEH2mElIxdd1kX27xx1LbXmHOXCbk4c%3D; _pst=jd_4ee26156e156b; __jda=116764038.1421839581.1652269721.1664081577.1664092157.283; __jdb=116764038.4.1421839581|283.1664092157; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
# ,'shsshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; areaId=4; ipLoc-djd=4-51026-58458-0; __jdv=116764038|direct|-|none|-|1662771596929; _s_id=gbn10972fc6ac4byqe61663806970020uq5c; logining=1; wlfstk_smdl=twvhwodqi0og9osrayyg9k8atgwn4fsx; TrackID=15J0qnZXBS8wO8Twxe8uit-1D2uuxAJyaPCPRY0HsWXA2ASTtzE8EfvQqqP-HCQ44ygqOAXdu3XhiN2aX5kDrE5arum9YOITd9RTWdkK5rOA; thor=23797F76015FE1D00FA6A8AD96F07FE23E5AEB02616E9132F794FF2D60A1ADDF6F8A7088FEDDF395376995F7747321EA6D10EE7B74DED54095172A67A0579B3D7EC07F7F3A6F05BE1078140D6B2F697BAC6EA5390457F8CAB8BDBA0F08F580E18D525EA73E82FDECC8BEAE4D972DCD395DB7E2C6A7929EAF5F5CB828117655C05B8DAA304598B7E28998F4162E2895CE; pinId=bosO_1BNpzkvZeF7erfaWA; pin=1843844151_m; unick=mslfour; ceshi3.com=000; _tp=O%2Bx6hgAFMhVV1E%2FsfxwpTQ%3D%3D; _pst=1843844151_m; gbn10972fc6ac4byqe61663806970020uq5c=108; __jda=116764038.1421839581.1652269721.1663979511.1664000828.280; __jdb=116764038.3.1421839581|280.1664000828; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
 # ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; areaId=4; ipLoc-djd=4-51026-58458-0; __jdv=116764038|direct|-|none|-|1662771596929; _s_id=kj66ohj3et2jwhn2imd1663201419327r1kx; logining=1; kj66ohj3et2jwhn2imd1663201419327r1kx=-359; wlfstk_smdl=goe9ex7uievqectze462batgx9wpsg09; TrackID=1SlOx423Rc7ShUdaz7N88V69T6JrxJbDNjzXbarx-BPc-G26mXeaV5qco82Zh2feGpQp_cdTsvD_FbSLKhu8QYcNi8145-2x43ky6wz9bvWg; thor=23797F76015FE1D00FA6A8AD96F07FE23E5AEB02616E9132F794FF2D60A1ADDF4EEB2C655D4BE112A8B17DCE0DE8DE54CDB2A07DC3F81C0B669AA1089330F144ACC52B5076D1707F34BB4A66823EF085B0C51546213957150C3CBF04DD6EFFACBBD4B504E5B99B94C152D1036B1BC207B0ADF938923C60CC8D3DAA1713DB30D89FBAFAE111743037F0F08E95D8AAF8F2; pinId=bosO_1BNpzkvZeF7erfaWA; pin=1843844151_m; unick=mslfour; ceshi3.com=000; _tp=O%2Bx6hgAFMhVV1E%2FsfxwpTQ%3D%3D; _pst=1843844151_m; __jda=116764038.1421839581.1652269721.1663426380.1663462900.270; __jdb=116764038.7.1421839581|270.1663462900; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
# ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; areaId=4; ipLoc-djd=4-51026-58458-0; __jdv=116764038|direct|-|none|-|1662771596929; _s_id=e0h1oontyocubj9wsku1662859457636u1ef; logining=1; e0h1oontyocubj9wsku1662859457636u1ef=100; wlfstk_smdl=zdi48o0v7wkpf7q4tncjmmpiax0oenqd; TrackID=1epyh84AoOcSFumU91Hj12IEW1R0cZF0jK-8YKVfsEIj1_KAiSUsGBuGfcYCYF_Bk9vlrwk-a7QJ_qFj6E9fdNgfnYVK8nz3JhAi-Pcjz3zM; thor=23797F76015FE1D00FA6A8AD96F07FE23E5AEB02616E9132F794FF2D60A1ADDF6FB1DE03C25A274CE75DA652AEB0A4C811B9EE7A06C43BCEA1BE02F8A17CD4E4CC735E7EAE6A6197A05B7F37FD6C396A13D74C8C9720B05B6BB4B35FF8A91D8BAE9FD44E19FF2B4E612B40F529159E04D5F6F30332E3871C423E38F94FA6C0B2600F48E77A68ABA6F60A48D1B9F9A81C; pinId=bosO_1BNpzkvZeF7erfaWA; pin=1843844151_m; unick=mslfour; ceshi3.com=000; _tp=O%2Bx6hgAFMhVV1E%2FsfxwpTQ%3D%3D; _pst=1843844151_m; __jda=116764038.1421839581.1652269721.1662968115.1663029060.260; __jdb=116764038.10.1421839581|260.1663029060; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
#  ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; __jdv=116764038|direct|-|none|-|1661475086014; areaId=4; ipLoc-djd=4-51026-58458-0; PCSYCityID=CN_500000_500100_0; _s_id=bu4xm20xrwcgd32x7u21662079120592u1rt; bu4xm20xrwcgd32x7u21662079120592u1rt=67; logining=1; wlfstk_smdl=zrie202ypwixb66j8nwzy5rnr9cql9pl; TrackID=1ga2laia2V_XYsHXT9M1VB3AC6J2mti6cIlnnUsigbLvMMuPK82LCuCnldbkcrH93O1b3gtRnk9bJCYYEV8Br_XRT8er4gVEh5p4edjL1WIc; thor=AE0D4789A4226F4BBB75E3F0154DBD2E0EE1E5CB2D359C95DA50046AECE1A86BDE73F6C3A37DC3B2585FD46AC8A05F2AFAE8E7221015C3EFCD86BAD8159523DF0C33654BD13E8ACD800CD73941192F6D6821EA15412EA1C477608F83FE413AE4F2CDA03653DF79F4E3AE535E21057F5E54B74C8CB8EF32A23A2DC9F2BD6822813B0FAAC272CD03E21069B8EF46D5B3D0ABFF0AF7C48C41AC8D04C9553646CB15; pinId=j5ErQ5GY8QnFlZhTFXLEqhKDwJD0f8E6; pin=jd_Vfj6NlzVbbReCGO; unick=jd_Vfj6NlzVbbReCGO; ceshi3.com=000; _tp=X1fFfY9uk4rXcM3EYx2zqD%2F9R9CSj9qp%2FjQMt%2FmSLWg%3D; _pst=jd_Vfj6NlzVbbReCGO; __jda=116764038.1421839581.1652269721.1661996483.1662079121.240; __jdb=116764038.8.1421839581|240.1662079121; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
#  ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; __jdv=116764038|direct|-|none|-|1661475086014; areaId=4; ipLoc-djd=4-51026-58458-0; PCSYCityID=CN_500000_500100_0; _s_id=bu4xm20xrwcgd32x7u21662079120592u1rt; bu4xm20xrwcgd32x7u21662079120592u1rt=67; logining=1; wlfstk_smdl=zrie202ypwixb66j8nwzy5rnr9cql9pl; TrackID=1ga2laia2V_XYsHXT9M1VB3AC6J2mti6cIlnnUsigbLvMMuPK82LCuCnldbkcrH93O1b3gtRnk9bJCYYEV8Br_XRT8er4gVEh5p4edjL1WIc; thor=AE0D4789A4226F4BBB75E3F0154DBD2E0EE1E5CB2D359C95DA50046AECE1A86BDE73F6C3A37DC3B2585FD46AC8A05F2AFAE8E7221015C3EFCD86BAD8159523DF0C33654BD13E8ACD800CD73941192F6D6821EA15412EA1C477608F83FE413AE4F2CDA03653DF79F4E3AE535E21057F5E54B74C8CB8EF32A23A2DC9F2BD6822813B0FAAC272CD03E21069B8EF46D5B3D0ABFF0AF7C48C41AC8D04C9553646CB15; pinId=j5ErQ5GY8QnFlZhTFXLEqhKDwJD0f8E6; pin=jd_Vfj6NlzVbbReCGO; unick=jd_Vfj6NlzVbbReCGO; ceshi3.com=000; _tp=X1fFfY9uk4rXcM3EYx2zqD%2F9R9CSj9qp%2FjQMt%2FmSLWg%3D; _pst=jd_Vfj6NlzVbbReCGO; __jda=116764038.1421839581.1652269721.1661996483.1662079121.240; __jdb=116764038.8.1421839581|240.1662079121; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
#  ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; shshshfp=c681c79d4ae263e3b7a5b3450e0d0668; __jdv=116764038|direct|-|none|-|1661475086014; areaId=4; ipLoc-djd=4-51026-58458-0; PCSYCityID=CN_500000_500100_0; _s_id=bu4xm20xrwcgd32x7u21662079120592u1rt; bu4xm20xrwcgd32x7u21662079120592u1rt=67; logining=1; wlfstk_smdl=zrie202ypwixb66j8nwzy5rnr9cql9pl; TrackID=1ga2laia2V_XYsHXT9M1VB3AC6J2mti6cIlnnUsigbLvMMuPK82LCuCnldbkcrH93O1b3gtRnk9bJCYYEV8Br_XRT8er4gVEh5p4edjL1WIc; thor=AE0D4789A4226F4BBB75E3F0154DBD2E0EE1E5CB2D359C95DA50046AECE1A86BDE73F6C3A37DC3B2585FD46AC8A05F2AFAE8E7221015C3EFCD86BAD8159523DF0C33654BD13E8ACD800CD73941192F6D6821EA15412EA1C477608F83FE413AE4F2CDA03653DF79F4E3AE535E21057F5E54B74C8CB8EF32A23A2DC9F2BD6822813B0FAAC272CD03E21069B8EF46D5B3D0ABFF0AF7C48C41AC8D04C9553646CB15; pinId=j5ErQ5GY8QnFlZhTFXLEqhKDwJD0f8E6; pin=jd_Vfj6NlzVbbReCGO; unick=jd_Vfj6NlzVbbReCGO; ceshi3.com=000; _tp=X1fFfY9uk4rXcM3EYx2zqD%2F9R9CSj9qp%2FjQMt%2FmSLWg%3D; _pst=jd_Vfj6NlzVbbReCGO; __jda=116764038.1421839581.1652269721.1661996483.1662079121.240; __jdb=116764038.8.1421839581|240.1662079121; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
# ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; unpl=JF8EAJtnNSttUB4BVksLSUIQHwldWwgMSUcGODcCVAgKGQcAEgJOE0R7XlVdXhRKER9sYBRXXlNOUA4eCysSEHteVV1ZDUgTAWdgNWRdWUpUBBwLGBsSe15Ublw4SxIAb24HXFlRS2Q1GwocIhBKXFVdVQ5CEwVnYjVkXGhLVQUaCisTIB0zVF9cCUoWBm9kBxldXUhUDBkKHxsQe1xkXQ; __jdv=116764038|direct|-|none|-|1660143776535; ipLoc-djd=25-2235-0-0; areaId=25; shshshfp=758983d0d8f1ad8c484ab42c13f0b29d; _s_id=vugd9rnuvcxskchncxq1660780961129wwso; logining=1; wlfstk_smdl=kn8rgt09ris5tv3sdemz1qa3vczlctqw; TrackID=1yJVxQKuGXs8lnTxh06XxfuG24c0j6zy-6I8VByOmBWD1CiQf6QvoXVfjOtnNBSppoSfqVtpsEER5rp6q8bIKytmteHaUNn1r7vQ-8-dCqIY; thor=6D375518B286DCBB9C151E4BA8D59FE82B4D91988513FFF099F2F370B9EDA78FABFD950905192070E302A36AD19CE943FBC770EF321C3502F0557352D76DE002CED2E5BB95CB2056CF3CD18FE0FDD650DB600DFD7F14890877ACD22B3BC1B2D05D07BBDBB79266AE686C5F32A2299BE0E1888477D279C1C783FF122B513C89162B80229A9F48F81B463E9409B53FA12BC92E1B0B01E3D555FBCC798DEAF298F4; pinId=uopmnhDtONwh-ZOCvyZcLrV9-x-f3wj7; pin=jd_4ee26156e156b; unick=shbiahkxinah1625; ceshi3.com=103; _tp=M0evnQ3Uww7FuEH2mElIxdd1kX27xx1LbXmHOXCbk4c%3D; _pst=jd_4ee26156e156b; __jda=116764038.1421839581.1652269721.1660694939.1660780962.202; __jdb=116764038.14.1421839581|202.1660780962; __jdc=116764038; vugd9rnuvcxskchncxq1660780961129wwso=461; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
# ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; _s_id=s4zdh71lf3lfortkl7916587049529004ddn; shshshfp=8d6dd7ee72cf132f10b725725d61c6ee; CCC_SE=ADC_MkP8ZrdHEA3fjTebywf%2bZ2YJ17qi0RQo6tsv5u1yuRaHLWsskf46QOW19fCDEQrlxrqSZQDpR3WxQkxxnerQEDBHsNdXUBRoBoBY6Q%2fLTyCI%2fbWOI69%2bKmalRXif%2bKCs894QsETSBv2n2CoDingAT77dDCJdo7KDfYYtEo3mwhJJoq9VmB7BTTqZRA2siVcZa%2bu0x2GPiL9yXaEwaUQoaTAeuZqytDFSZ1OFx%2fVqOC%2f9zPR4UfUOagRUF4WA%2fUi%2bkLFdTP6jkXHA5fMtw3Xl1z7MgYlfFd8Bdw0jJpb2oNCR%2b973lEor0HJ64K%2bnNO5rpGDYhM8QfbcWBppQ33qpyjDbO0iXyiEdHAIjXH6QADjZxLcw75Wf0VoWzc%2f9hfJIqDU9G2jN4yKP0OaTQHHWpn4cQOUvBjcUvYHkDkotr4UvUQ1BBYmrNQTmayxY4K5aitPE1QF%2fgm5WIRUmfi96be22K%2fGGECxFyxapvE4%2fRIo%3d; unpl=JF8EAJtnNSttUB4BVksLSUIQHwldWwgMSUcGODcCVAgKGQcAEgJOE0R7XlVdXhRKER9sYBRXXlNOUA4eCysSEHteVV1ZDUgTAWdgNWRdWUpUBBwLGBsSe15Ublw4SxIAb24HXFlRS2Q1GwocIhBKXFVdVQ5CEwVnYjVkXGhLVQUaCisTIB0zVF9cCUoWBm9kBxldXUhUDBkKHxsQe1xkXQ; __jdv=122270672|www.lujd.club|t_2025425396_|jingfen|9ddba8ca1ee84d53a4fa61dccb481d0e|1658846749375; areaId=25; ipLoc-djd=25-2235-0-0; logining=1; s4zdh71lf3lfortkl7916587049529004ddn=263; wlfstk_smdl=hse9bru3airll3c6mal2guhj87zhr909; TrackID=1YQEzliA6XPHbXNnkDhF5XBvAPlJR-M-qHoFrXtiYLzovVivwu4ApADDAdEX5jx4-YatcitcuVs5po6g-ecitKn5RAtpINmhbjRq9ZNbMcBM; thor=AE0D4789A4226F4BBB75E3F0154DBD2E0EE1E5CB2D359C95DA50046AECE1A86B3935773E0A4D2268EAE05B19B9A41E39DF926DB0B0C456A0AE9F2942083294F4E8BB6C5CB8898B698AFC319CC06E87D27731693DA1FFB5EA4FAF569B4650918EB6E3E86028A3C0B453A135C6590C9D16456EA861E75B4D99DAB233A066D4E1D7F514CF29B5C2782A2141497DCC2E1B08057E778F4AE72F01BFA95907D1F92A89; pinId=j5ErQ5GY8QnFlZhTFXLEqhKDwJD0f8E6; pin=jd_Vfj6NlzVbbReCGO; unick=jd_Vfj6NlzVbbReCGO; ceshi3.com=000; _tp=X1fFfY9uk4rXcM3EYx2zqD%2F9R9CSj9qp%2FjQMt%2FmSLWg%3D; _pst=jd_Vfj6NlzVbbReCGO; __jda=116764038.1421839581.1652269721.1659397744.1659484749.172; __jdb=116764038.7.1421839581|172.1659484749; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
# ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; user-key=3c7b427a-f692-454e-8b21-b823471a75af; shshshfp=fd2e85f09cfdcc74983f0d1707a7a225; __jdv=122270672|direct|-|none|-|1657282965661; _s_id=whqw3bxu63ftwhxkjfk16581581340348n1s; areaId=4; ipLoc-djd=4-51026-0-0; logining=1; whqw3bxu63ftwhxkjfk16581581340348n1s=139; wlfstk_smdl=caci93o4pkwd2pav9pkqynz623y6uos6; TrackID=1rj0hBAU3uZ_wHyMdIaHKPjh66XZnoFEvNotsFJTw7Jwt1E2qUuP01t7z-7xSGxZGyfRImZkET1_zN5iJ41Xjm3StU131QzHUTDBzySL99aQ; thor=6D375518B286DCBB9C151E4BA8D59FE82B4D91988513FFF099F2F370B9EDA78FDC2C14AE7348ADF3D2A2DB61CDC016ADB52D97FF7A5FEC7B99499404F6CAA4206F3D34D6BAE84339F9251CE0DB7FD9EE951C5AA1F0903C7E30EC209979374A877CE1C3BE742F5A88BF86CCB27489CFD54C19A60417B6A60EA7343F4FDDD41F753252D81A2064F158BC167074BC67F71AAAA25036A0F64C36CFBF1C223D4AA928; pinId=uopmnhDtONwh-ZOCvyZcLrV9-x-f3wj7; pin=jd_4ee26156e156b; unick=shbiahkxinah1625; ceshi3.com=103; _tp=M0evnQ3Uww7FuEH2mElIxdd1kX27xx1LbXmHOXCbk4c%3D; _pst=jd_4ee26156e156b; __jda=116764038.1421839581.1652269721.1658232448.1658278729.144; __jdb=116764038.9.1421839581|144.1658278729; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
# ,'shshshfpa=4c1e8652-5628-1e61-26d0-bf867d00ca33-1635155537; __jdu=1421839581; shshshfpb=ii2ppF2orcWB6Kys%2BtxxKYw%3D%3D; _c_id=9g7stjbf0q0frs84iva1655986535261k1mo; user-key=3c7b427a-f692-454e-8b21-b823471a75af; shshshfp=fd2e85f09cfdcc74983f0d1707a7a225; __jdv=122270672|direct|-|none|-|1657282965661; _s_id=d8u00wsfv9slnc39n0616579267211274pcs; logining=1; d8u00wsfv9slnc39n0616579267211274pcs=277; wlfstk_smdl=h417n369vrninbahqp70h5nl59wq1ydj; TrackID=1C73YBd0TqRQJeNo-v2nLKihPh0DvZH6qvoHaSl17KiFBx5E1fCwQVXRjIO-sqdJXVpW7i8dS_aShpIwt58CkktO9ciOkBmnkbP5Oj9NfINQ; thor=AE0D4789A4226F4BBB75E3F0154DBD2E0EE1E5CB2D359C95DA50046AECE1A86BDE73F6C3A37DC3B2585FD46AC8A05F2AA5CC34ACCD20C8AC18BE5AA3DE6AD602D05693D42DCC7F007700EEA6D21FB692F80EC47ACC9437324A757946C7F4355CD330BA37D882F7AA44077F038096F32ED39C06CCBD105B4191DE45A8B5479B1568636383006CA21F47A46C132E9FFD8F0EB5218F760B4DBB6D3902A2235A3E56; pinId=j5ErQ5GY8QnFlZhTFXLEqhKDwJD0f8E6; pin=jd_Vfj6NlzVbbReCGO; unick=jd_Vfj6NlzVbbReCGO; ceshi3.com=000; _tp=X1fFfY9uk4rXcM3EYx2zqD%2F9R9CSj9qp%2FjQMt%2FmSLWg%3D; _pst=jd_Vfj6NlzVbbReCGO; __jda=116764038.1421839581.1652269721.1658058509.1658102523.138; __jdb=116764038.11.1421839581|138.1658102523; __jdc=116764038; 3AB9D23F7A4B3C9B=YXAQDK7TWQNJ6ZGMVHB5TUFELHIKE4GWFM64MI625ABZEZHGT3QE6OYSC2VX3WBC2NWAHDLOMBI5W2LBIFI4S443ZE'
]
remaining_times=440 #毫秒
addtimes=20

Referer='https://1paipai.jd.com/auction-detail/337582691'
file_path=r"C:\Users\Administrator\Desktop\DBD自动化价目匹配表\goods_price.xls" #excle数据地址
#获取提醒列表商品,user是整数代表cookie_list中的顺序对应账号的cookie
def reminder_list(user):
    HEADERS = {
    'Referer': 'https://paipai.m.jd.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'Cookie': 'coo'
    }
    #获取账号cookie
    HEADERS['Cookie'] =cookie_list[int(user)]
    new_list=[]
    for i in range(1,6):
        url='https://api.m.jd.com/api?functionId=paipai.dbd.reminder.auctionList&body=%7B%22readStatus%22:%22%22,%22endStatus%22:%220%22,%22pageNo%22:{},%22pageSize%22:20,%22mpSource%22:1,%22sourceTag%22:2%7D&t=1657766703158&appid=paipai_h5'.format(str(i))
        r = requests.get(url, headers=HEADERS)
        id_list = re.findall(r"id\":(.+?)\,", r.text)
        if len(id_list)==0:
            break
        name_list = re.findall(r"productName\":(.+?)\,", r.text)
        end_list = re.findall(r"endTime\":(.+?)\,", r.text)
        orginal_price=re.findall(r"maxPrice\":(.+?)\,", r.text)
        for j in range(len(id_list)):
            list=[]
            list_c=i*20-20+j
            list.append(id_list[j])
            list.append(int(end_list[j]))
            list.append(name_list[j].replace('\"',''))
            timeStamp = int(end_list[j]) / 1000
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            list.append(otherStyleTime)
            list.append(int(float(orginal_price[j])))
            new_list.append(list)
        if len(id_list)<20:
            break
    #新出价商品
    HEADERS['Cookie'] = cookie_list[int(user)+1]
    url = 'https://api.m.jd.com/api?functionId=dbd.record.myRecords&body=%7B%22showStatus%22:-1,%22pageSize%22:15,%22pageNum%22:1%7D&t=1660145102279&appid=paipai_h5'
    response = requests.get(url, headers=HEADERS)
    # print(response.text)
    # print('新ID', response.text)
    id_list = re.findall(r"auctionId\":(.+?)\,", response.text)
    print('新ID',id_list)
    name_list = re.findall(r"productName\":(.+?)\,", response.text)
    end_list = re.findall(r"endTime\":(.+?)\,", response.text)
    orginal_price = re.findall(r"maxPrice\":(.+?)\,", response.text)
    if id_list :
        remaid_len = len(new_list)
        for j in range(len(new_list),len(new_list)+3):
            if j>=remaid_len+3:
                break
            timeStamp = int(end_list[i]) / 1000
            # if timeStamp<time.time():
            #     continue
            list = []
            i= j-remaid_len
            list.append(id_list[i])
            list.append(int(end_list[i]))
            list.append(name_list[i].replace('\"', ''))
            timeStamp = int(end_list[i]) / 1000
            # if timeStamp<time.time():
            #     break
            timeArray = time.localtime(timeStamp)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            list.append(otherStyleTime)
            if orginal_price[i] == 'null':
                orginal_price[i]=0
            list.append(int(float(orginal_price[i])))
            if timeStamp>time.time():
                new_list.append(list)

    return new_list
#获取excel价格表数据
def read_excel(a):
    file = xlrd.open_workbook(a)
    table = file.sheet_by_name('Sheet1')  ##用工作表的名称来调取需要读取的数据，这里需要Sheet1里的数据
    excel_data = []
    for i in range(1, table.nrows):
        row_data = table.row_values(i)
        excel_data.append(row_data)
    excel_data = np.array(excel_data)
    excel_data=excel_data.tolist()
    return excel_data
#获取商品名称
def get_goodname(ID):
    HEADERS = {
        'Referer': 'https://paipai.m.jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Cookie': 'coo'
    }
    # 获取账号cookie
    HEADERS['Cookie'] = cookie_list[0]
    HEADERS['Referer'] =Referer
    r_url = 'https://used-api.jd.com/auction/detail?auctionId=' + ID + '&callback=__jp1'
    r = requests.get(r_url, headers=HEADERS)
    endtime_json = r.text.replace('/**/__jp1(', '').replace('});', '}')
    with open('goods_name.json', 'w', encoding='utf-8') as fp:
        fp.write(endtime_json)
    endtime_obj = json.load(open('goods_name.json', 'r', encoding='utf-8'))
    # 商品名称
    product_name = jsonpath.jsonpath(endtime_obj, '$..productName')[0]
    return product_name

#夺宝商品list和定价策略
def db_goods_strategy(new_list,excel_data):
    strategy_list=[]
    for i in range(len(new_list)):
        for j in range(len(excel_data)+1):
            if j == len(excel_data):
                c = ['1','0', '0']
                c.insert(1,int(new_list[i][4]*0.8))
                strategy_list.append(new_list[i] + c)
                break
            a=new_list[i][2]
            b=excel_data[j][0]
            if a.find(b) >=0:
                strategy_list.append(new_list[i]+excel_data[j][1:])
                break
        strategy_list=sorted(strategy_list, key=lambda x: x[1])
    return strategy_list
def get_curprice(ID,cookie):
    HEADERS = {
        'Referer': 'https://paipai.m.jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Cookie': 'coo'
    }
    # 获取账号cookie
    HEADERS['Cookie'] = cookie
    HEADERS['Referer'] = Referer
    p_url = 'https://used-api.jd.com/auctionRecord/getCurrentAndOfferNum?auctionId=' + ID + '&callback=__jp17'
    p = requests.get(p_url, headers=HEADERS)
    cur_price = re.findall(r"currentPrice\":(.+?),", p.text)
    cur_price = ''.join(cur_price)
    # 判断价格
    if cur_price == 'null':
        cur_price ='1'
    else :
        pass
    return cur_price
def get_request_times(ID):
    a=time.time()*1000
    HEADERS = {
        'Referer': 'https://paipai.m.jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Cookie': 'coo'
    }
    # 获取账号cookie
    HEADERS['Cookie'] = cookie_list[1]
    HEADERS['Referer'] = Referer
    p_url = 'https://used-api.jd.com/auctionRecord/getCurrentAndOfferNum?auctionId=' + ID + '&callback=__jp17'
    p = requests.get(p_url, headers=HEADERS)
    cur_price = re.findall(r"currentPrice\":(.+?),", p.text)
    cur_price = ''.join(cur_price)
    # 判断价格
    if cur_price == 'null':
        cur_price ='1'
    else :
        pass
    c=int(time.time()*1000-a)
    return c
#出价
def buy(cookie,ID,price):
    buy_url = 'https://used-api.jd.com/auctionRecord/offerPrice'
    HEADERS = {
        'Referer': 'https://paipai.m.jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Cookie': 'coo'
    }
    # 获取账号cookie
    HEADERS['Cookie'] = cookie
    HEADERS['Referer'] =Referer
    data = {
        'trackId': '3b154f3a78a78f8b6c2eea5a3cee5674',
        'eid': 'UTT4AVFUIZFVD6KGHHJRAGEEGFJ4MWFSOPDUEF7KBEHDA5ODK3GKDKP5PCVTWIAQ32N2ZT2AR5YBAH3T27354OAI3Q',

    }
    data['price'] = str(int(price))
    data['auctionId'] = str(ID)
    # print(data)
    resp = requests.post(buy_url, headers=HEADERS, data=data)
    print('已经出价',str(price))
    print(resp.json())


new_list=reminder_list(0)
for i in range(len(new_list)):
    good_id=new_list[i][0]
    good_name=get_goodname(good_id)
    new_list[i][2]=good_name
excel_data=read_excel(file_path)
goods_strategy_list=db_goods_strategy(new_list,excel_data)
for i in range(len(goods_strategy_list)):
    print(goods_strategy_list[i][0:1]+goods_strategy_list[i][3:8],str(goods_strategy_list[i][2]))
for i in range(len(goods_strategy_list)):
    print(str(goods_strategy_list[i][2]))
#准备夺宝商品列表和匹配对应价格策略
try:
    while True:
        new_list = reminder_list(0)
        for i in range(len(new_list)):
            good_id = new_list[i][0]
            good_name = get_goodname(good_id)
            new_list[i][2] = good_name
        excel_data = read_excel(file_path)
        goods_strategy_list = db_goods_strategy(new_list, excel_data)
        for i in range(len(goods_strategy_list)):
            print(goods_strategy_list[i][0:1] + goods_strategy_list[i][3:8], str(goods_strategy_list[i][2]))
        for i in range(len(goods_strategy_list)):
            print(str(goods_strategy_list[i][2]))
        new_list=reminder_list(0)
        #当提醒列表为空时停止程序
        if len(new_list)==0:
            break
        for i in range(len(new_list)):
            good_id=new_list[i][0]
            time.sleep(0.1)
            good_name=get_goodname(good_id)
            new_list[i][2]=good_name
        excel_data=read_excel(file_path)
        goods_strategy_list=db_goods_strategy(new_list,excel_data)
        for i in range(len(goods_strategy_list)):
            print(goods_strategy_list[i][0:1] + goods_strategy_list[i][3:8], str(goods_strategy_list[i][2]))
        for i in range(len(goods_strategy_list)):
            rand = random.randint(1,len(cookie_list)-1)
            cookie = cookie_list[rand]
            data_list=goods_strategy_list[i]
            if   data_list[1]>time.time()*1000:
            #是否一口价商品
                one_price_good = str(data_list[7])
            #商品ID
                goods_id= str(data_list[0])
            #加价金额
                goods_add_price = float(data_list[5])
            #期望价格
                goods_my_price =  float(data_list[6])
            #而外预算金额
                goods_outside_price = float(data_list[8])
            #结束时间戳
                endtimes= data_list[1]
            #获取请求反应时间
                remaining_times=get_request_times(goods_id)*2+addtimes
                print('remaining_times等于：',remaining_times)
                print('夺宝商品:', data_list[2])
                print('结束时间:', data_list[3])
                print('沉睡时间', str((endtimes - time.time() * 1000 - remaining_times) / 1000) + 's')
                sleeps=(endtimes - time.time() * 1000 - remaining_times ) / 1000
                if sleeps >1 and sleeps>1800:
                    time.sleep(1500)
                    break
                elif  sleeps >1:
                    time.sleep((endtimes - time.time() * 1000 -5000 ) / 1000)
                    remaining_times = get_request_times(goods_id) * 2 + addtimes
                    print('remaining_times等于：', remaining_times)
                    print(endtimes - time.time() * 1000 - remaining_times)
                    time.sleep((endtimes - time.time() * 1000 - remaining_times) / 1000)
                print('距离结束还有'+str((endtimes - time.time() * 1000) / 1000)+'s')
            # 获取当前价格
                x = get_curprice(goods_id,cookie)
                x = float(x)
                my_price=0
                print('当前价格',x)
                # if goods_my_price >= (x + goods_add_price) or str(int(one_price_good)) == '1':
                if goods_my_price >= (x + goods_add_price):
                    if (str(int(one_price_good)) == '1') and (goods_outside_price > x) :
                        buy(cookie,goods_id,goods_outside_price+1)
                        my_price=goods_outside_price+1
                    elif (str(int(one_price_good)) == '1') and (goods_outside_price <= x):
                        buy(cookie,goods_id,x+goods_add_price)
                        my_price = x+goods_add_price
                    else:
                        buy(cookie,goods_id,x + goods_add_price)
                        my_price=x + goods_add_price
                print('距离结束', str((endtimes - time.time() * 1000) / 1000) + 's')
                time.sleep(0.5)
                cj_price=get_curprice(goods_id,cookie)
                print('我的价格:',my_price)
                print('成交价格:',cj_price)
                if float(my_price) == float(cj_price):
                    engine = pyttsx3.init()
                    engine.setProperty("voice","HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ZH-CN_HUIHUI_11.0")
                    chinese = '来付款，王霄翰'
                    print('抢单成功')
                    engine.say(chinese)
                    engine.runAndWait()
                endtimes = float(time.time())
                timeStamp = int(endtimes)
                timeArray = time.localtime(timeStamp)
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                print('目前时间:', otherStyleTime)
                print('开始下一个')
                break
            else:
                print('已过期','开始下一个')
                break
except KeyboardInterrupt:
    print('已停止')