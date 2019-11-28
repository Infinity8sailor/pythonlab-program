import wget
import os
path1="/Users/vaibhav/Desktop/database/cet2020/CAP3/"
file=open("/Users/vaibhav/Desktop/database/cet2020/CAP3/reg_no_college.txt","a")
data=[1002, 1005, 1012, 1101, 1105, 1107, 1114, 1116, 1117, 1119, 1120, 1121, 1123, 1125, 1126, 1127, 1128, 1129, 1130, 1148, 1180, 1182, 1265, 1268, 1276, 2008, 2020, 2021, 2111, 2112, 2113, 2114, 2116, 2126, 2127, 2128, 2129, 2130, 2131, 2132, 2133, 2134, 2135, 2136, 2137, 2138, 2141, 2146, 2250, 2252, 2254, 2516, 2522, 2533, 2573, 3012, 3014, 3033, 3035, 3036, 3135, 3139, 3146, 3148, 3154, 3174, 3175, 3176, 3181, 3182, 3183, 3184, 3185, 3187, 3188, 3189, 3190, 3192, 3193, 3194, 3196, 3197, 3198, 3199, 3200, 3201, 3202, 3203, 3204, 3207, 3209, 3210, 3211, 3214, 3215, 3216, 3217, 3218, 3219, 3220, 3221, 3222, 3223, 3224, 3351, 3353, 3423, 3436, 3439, 3445, 3447, 3460, 3462, 3465, 3467, 3471, 3475, 3477, 3503, 4004, 4005, 4025, 4104, 4115, 4116, 4118, 4123, 4133, 4134, 4136, 4137, 4138, 4139, 4141, 4142, 4143, 4144, 4145, 4147, 4151, 4163, 4167, 4171, 4172, 4174, 4175, 4177, 4178, 4179, 4181, 4186, 4187, 4188, 4190, 4192, 4193, 4195, 4196, 4197, 4285, 4302, 4304, 4613, 4649, 5003, 5004, 5103, 5104, 5106, 5107, 5108, 5109, 5121, 5124, 5125, 5130, 5139, 5151, 5152, 5160, 5161, 5162, 5164, 5168, 5169, 5170, 5171, 5172, 5173, 5176, 5177, 5179, 5181, 5182, 5184, 5303, 5322, 5330, 5331, 5381, 5382, 5390, 5396, 5399, 5401, 5408, 5409, 5411, 5418, 5449, 6004, 6005, 6006, 6007, 6028, 6122, 6138, 6139, 6141, 6144, 6145, 6146, 6149, 6155, 6156, 6160, 6175, 6176, 6177, 6178, 6179, 6182, 6183, 6184, 6185, 6187, 6203, 6206, 6207, 6214, 6217, 6219, 6220, 6222, 6223, 6250, 6265, 6267, 6268, 6269, 6271, 6272, 6273, 6274, 6275, 6276, 6277, 6278, 6281, 6282, 6284, 6285, 6288, 6289, 6293, 6298, 6303, 6304, 6305, 6307, 6308, 6310, 6311, 6313, 6315, 6317, 6318, 6319, 6320, 6321, 6322, 6323, 6324, 6326, 6419, 6466, 6545, 6609, 6620, 6622, 6625, 6628, 6632, 6634, 6635, 6640, 6643, 6644, 6649, 6732, 6754, 6755, 6756, 6757, 6758, 6759, 6762, 6766, 6767, 6768, 6769, 6770, 6772, 6780, 6781, 6782, 6787, 6794, 6795, 6796, 6797, 6802, 6803, 6809, 6815, 6822, 6834, 6839, 6878, 6901, 6938]

for num in data:
    print(num)
    if os.path.exists("/Users/vaibhav/Desktop/database/cet2020/CAP3/CAPR-III_EN"+str(num)+".pdf"):
        pass
    else:
        try:
            wget.download("http://fe2019.mahacet.org/CAP-III/CAPR-III_EN"+str(num)+".pdf",path1)
            file.write(str(num)+",")
            
        except Exception:
            print("error")
            pass
    