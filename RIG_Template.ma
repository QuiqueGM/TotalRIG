//Maya ASCII 2019 scene
//Name: Arxiu 001 - Base.ma
//Last modified: Tue, May 30, 2023 11:36:15 AM
//Codeset: 1252
requires maya "2019";
requires "stereoCamera" "10.0";
currentUnit -l meter -a degree -t ntscf;
fileInfo "application" "maya";
fileInfo "product" "Maya 2019";
fileInfo "version" "2019";
fileInfo "cutIdentifier" "202003131251-bd5bbc395a";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19045)\n";
fileInfo "UUID" "73CA08D5-4D2F-EB69-F6CC-FA8AFCC18D91";
createNode transform -s -n "persp";
	rename -uid "B8642AF9-46A2-74A7-419F-EDA496B9AB4F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 2.422488238311169 0.93179860594450059 0.76497842076491529 ;
	setAttr ".r" -type "double3" -19.538352741346035 -1729.0000000011703 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "7CE1E332-43C2-D480-88C1-7FB3839E65EF";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".ncp" 0.001;
	setAttr ".fcp" 100;
	setAttr ".fd" 0.05;
	setAttr ".coi" 2.5953009988931046;
	setAttr ".ow" 0.1;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0 -4.4408920985006262e-16 0 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "7AF49BC6-47CF-576B-29EB-88A70E2E8E80";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1.3870948990694592 10.112032840912201 -0.10152664669227089 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "63FE3E93-40F1-C6C5-F37A-0B8873FFB7A4";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.001;
	setAttr ".fcp" 100;
	setAttr ".fd" 0.05;
	setAttr ".coi" 9.4045066720889583;
	setAttr ".ow" 1.4898781326940935;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 117.90160369873047 70.75261688232419 4.1965103149414418 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "8E70AF66-4100-92D9-7381-FA8D779E5799";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.1183973420522661 0.66856564387308193 10.066385589757251 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "9BA9B2F5-49EB-791B-C6AD-30965E573E91";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.001;
	setAttr ".fcp" 100;
	setAttr ".fd" 0.05;
	setAttr ".coi" 9.6619077073719968;
	setAttr ".ow" 3.3903900390590076;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 22.500972747802734 1.9245245456695548 40.447788238525398 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "15FFE1A3-47D8-C9A6-0266-88B6CEBD056D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 10.21371091028209 0.45456188201904291 -0.25390388488769533 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "85FD1E25-4732-61B7-2D41-169E141716B1";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.001;
	setAttr ".fcp" 100;
	setAttr ".fd" 0.05;
	setAttr ".coi" 10.21371091028209;
	setAttr ".ow" 1.2294804663346814;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 0 45.45618820190429 -25.390388488769531 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "JointsReference";
	rename -uid "2C2A2477-449B-E363-7BA0-9798024379C0";
createNode transform -n "JR_000" -p "JointsReference";
	rename -uid "DFBDDD93-4E2C-84B9-D354-FEA6A25EB87F";
createNode locator -n "JR_000Shape" -p "JR_000";
	rename -uid "E9787D0D-4545-FC07-6185-28BC87144BC8";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" -7.9936057773011278e-19 -6.3948846218409015e-18 -7.3163321771600212e-35 ;
	setAttr ".los" -type "double3" 0.00025 0.00025 0.00025 ;
createNode transform -n "BR_Sphere" -p "JR_000";
	rename -uid "5464D089-4D0B-406E-8F10-15834A547555";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode nurbsCurve -n "nurbsCircleShape1" -p "BR_Sphere";
	rename -uid "8230656C-46B8-1DCC-5236-9594D75BBBE2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.011754174373368367 -7.0334537974861747e-17 -0.011754174373368387
		1.0178598484666368e-18 -7.0036413727543378e-17 -0.016622912813315835
		-0.011754174373368367 -7.0334537974861747e-17 -0.011754174373368382
		-0.016622912813315821 -7.105427357601002e-17 -1.8625303129631228e-17
		-0.011754174373368367 -7.1774009177158294e-17 0.011754174373368349
		-1.6651285454404838e-18 -7.207213342447665e-17 0.016622912813315807
		0.011754174373368367 -7.1774009177158294e-17 0.011754174373368348
		0.016622912813315821 -7.105427357601002e-17 -1.5496707642832567e-17
		0.011754174373368367 -7.0334537974861747e-17 -0.011754174373368387
		1.0178598484666368e-18 -7.0036413727543378e-17 -0.016622912813315835
		-0.011754174373368367 -7.0334537974861747e-17 -0.011754174373368382
		;
	setAttr ".hio" yes;
createNode nurbsCurve -n "nurbsCircleShape2" -p "BR_Sphere";
	rename -uid "755199E0-41BA-872B-A2BD-8195CF185275";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.011754174373368367 0.011754174373368299 -1.7043832792854235e-17
		1.0178598484666368e-18 0.016622912813315745 -1.6745708545535866e-17
		-0.011754174373368367 0.011754174373368294 -1.7043832792854235e-17
		-0.016622912813315821 -7.0192538840381297e-17 -1.7763568394002505e-17
		-0.011754174373368367 -0.011754174373368438 -1.8483303995150775e-17
		-1.6651285454404838e-18 -0.016622912813315897 -1.8781428242469144e-17
		0.011754174373368367 -0.011754174373368436 -1.8483303995150775e-17
		0.016622912813315821 -7.3321134327179949e-17 -1.7763568394002505e-17
		0.011754174373368367 0.011754174373368299 -1.7043832792854235e-17
		1.0178598484666368e-18 0.016622912813315745 -1.6745708545535866e-17
		-0.011754174373368367 0.011754174373368294 -1.7043832792854235e-17
		;
	setAttr ".hio" yes;
createNode nurbsCurve -n "nurbsCircleShape3" -p "BR_Sphere";
	rename -uid "819E74EF-44BB-D897-6B01-818DBB82331B";
	setAttr -k off ".v";
	setAttr ".sech" no;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		7.1973560114827106e-19 0.011754174373368299 -0.011754174373368384
		1.017859848466637e-18 0.016622912813315745 -1.8781428242469141e-17
		7.1973560114827067e-19 0.011754174373368294 0.011754174373368349
		5.2766034285090406e-35 -7.0192538840381297e-17 0.016622912813315804
		-7.1973560114827087e-19 -0.011754174373368438 0.011754174373368349
		-1.0178598484666376e-18 -0.016622912813315897 -1.609843984856202e-17
		-7.1973560114827067e-19 -0.011754174373368436 -0.011754174373368384
		-1.3880518815165148e-34 -7.3321134327179949e-17 -0.016622912813315842
		7.1973560114827106e-19 0.011754174373368299 -0.011754174373368384
		1.017859848466637e-18 0.016622912813315745 -1.8781428242469141e-17
		7.1973560114827067e-19 0.011754174373368294 0.011754174373368349
		;
	setAttr ".hio" yes;
createNode transform -n "Controllers";
	rename -uid "AEDB31D0-4BF7-ACCD-6A10-28926B0265E0";
createNode transform -n "CTRL__Master" -p "Controllers";
	rename -uid "500C9032-4954-4038-A048-8697B8ED722F";
createNode nurbsCurve -n "CTRL__MasterShape" -p "CTRL__Master";
	rename -uid "9FD897DA-4DDE-BDE6-2990-D99E67987935";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.86197280883789063 5.2780613470841501e-17 -0.86197280883789063
		7.4643058999902292e-17 7.4643058999902292e-17 -1.219013671875
		-0.86197280883789063 5.2780613470841501e-17 -0.86197280883789063
		-1.219013671875 3.8695094662543283e-33 -6.3193879823290635e-17
		-0.86197280883789063 -5.2780613470841501e-17 0.86197280883789063
		-1.2210943011131767e-16 -7.4643058999902292e-17 1.219013671875
		0.86197280883789063 -5.2780613470841501e-17 0.86197280883789063
		1.219013671875 -1.0179047569646096e-32 1.6623645006114825e-16
		0.86197280883789063 5.2780613470841501e-17 -0.86197280883789063
		7.4643058999902292e-17 7.4643058999902292e-17 -1.219013671875
		-0.86197280883789063 5.2780613470841501e-17 -0.86197280883789063
		;
createNode transform -n "Rig";
	rename -uid "A396D315-43B6-CB82-AE89-87998615BD48";
createNode transform -n "Helpers";
	rename -uid "A0509405-4E05-8E8B-819F-189E7191EB0B";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "A15F907D-4567-C787-3435-72A6F848ED97";
	setAttr -s 12 ".lnk";
	setAttr -s 12 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "54F4C7F7-4CC1-5CD7-DC68-8FA58271443E";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 0 ;
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "5C445637-4EFA-B7B3-B936-94BB76EAA9F9";
createNode displayLayerManager -n "layerManager";
	rename -uid "FA9DB58E-431A-52F9-F319-0299B3CAE1B4";
	setAttr ".cdl" 1;
	setAttr -s 10 ".dli[1:9]"  1 3 2 4 5 10 7 8 
		9;
	setAttr -s 6 ".dli";
createNode displayLayer -n "defaultLayer";
	rename -uid "68F3BEE6-4D46-57C7-E0D0-2CB87F216394";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "F277936C-43CE-8ECA-E7B5-0C81D26879A9";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "C46F5D4D-4299-557B-66FB-FEAC3FF0A3F4";
	setAttr ".g" yes;
createNode phong -n "A_Fire";
	rename -uid "FAD1689D-43D6-9385-639D-D9AC4E79ADC7";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "Flame_AdultSG";
	rename -uid "B4EC7848-4E73-7589-123F-48A21F046196";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo1";
	rename -uid "3F120CE9-405A-423D-4CFB-458BF7F06FDC";
createNode file -n "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037";
	rename -uid "971F1357-4F3E-B7A7-5FFC-2BA713AA56A6";
	setAttr ".ftn" -type "string" "D:/SOCIAL_POINT/DragonCity2/ExternalResources/Fire_Adult/TEX_CHR_A_Fire_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture1";
	rename -uid "6EF55445-4EBC-5B94-4F94-EF8A9C2516AF";
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "04A8AE69-4FE6-CF8A-2ABD-DC95D9977303";
	setAttr ".b" -type "string" "playbackOptions -min 0 -max 200 -ast 0 -aet 200 ";
	setAttr ".st" 6;
createNode phong -n "A_Fire1";
	rename -uid "AEA15909-4A6C-5A22-678B-61B05C78D105";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "Flame_AdultSG1";
	rename -uid "3E53B607-4C66-B45D-4052-7F9261E7C68F";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo2";
	rename -uid "85912371-4DB2-5218-9E42-F093B226011C";
createNode file -n "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038";
	rename -uid "1AA706C2-4E64-CB48-8D02-BAA09485436F";
	setAttr ".ftn" -type "string" "D:/SOCIAL_POINT/DragonCity2/ExternalResources/DragonsRef/Textures/TEX_CHR_A_Fire_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture2";
	rename -uid "2F680158-4959-7FCA-910D-EBA1649471F1";
createNode phong -n "_Fire_Adult_BLENDSHADES:A_Fire";
	rename -uid "BEDE6DBF-45EE-7506-A402-9DBDED3214DB";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "_Fire_Adult_BLENDSHADES:Flame_AdultSG";
	rename -uid "D34EF31F-4310-6667-839A-2A8703B7E14A";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "_Fire_Adult_BLENDSHADES:materialInfo1";
	rename -uid "5EFD7461-4F87-DA5F-FB74-D28BCADD8C2D";
createNode file -n "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037";
	rename -uid "1FED792A-4C68-3899-7988-789642C50A00";
	setAttr ".ftn" -type "string" "D:/SOCIAL_POINT/DragonCity2/ExternalResources/Fire_Adult/TEX_CHR_A_Fire_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "_Fire_Adult_BLENDSHADES:place2dTexture1";
	rename -uid "D2389E23-4403-A50A-6E0F-B885D28BFC2D";
createNode phong -n "_Fire_Adult_BLENDSHADES:A_Fire1";
	rename -uid "B48CBCC5-4233-65FE-6721-02BA5E8E811D";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "_Fire_Adult_BLENDSHADES:Flame_AdultSG1";
	rename -uid "1F8A2833-49DD-5242-7576-65B113D9CBC8";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "_Fire_Adult_BLENDSHADES:materialInfo2";
	rename -uid "EFFABD34-477A-4A71-A409-57A5C55E5B8B";
createNode file -n "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038";
	rename -uid "C759D2C0-4013-2F51-CDE5-82BC044A5815";
	setAttr ".ftn" -type "string" "D:/SOCIAL_POINT/DragonCity2/ExternalResources/DragonsRef/Textures/TEX_CHR_A_Fire_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "_Fire_Adult_BLENDSHADES:place2dTexture2";
	rename -uid "85851C35-44DA-C79C-6D2D-A1AE970168E4";
createNode displayLayer -n "GEOMETRY";
	rename -uid "598009AB-445B-213E-B6D8-23991C0D550A";
	setAttr ".hpb" yes;
	setAttr ".c" 18;
	setAttr ".do" 1;
createNode displayLayer -n "JOINTS_REF";
	rename -uid "C23C8F60-4D99-5A9E-E619-629099E51204";
	setAttr ".hpb" yes;
	setAttr ".c" 31;
	setAttr ".do" 2;
createNode displayLayer -n "JOINTS";
	rename -uid "816B673E-4E88-7060-EDF9-29BA4A14CEB4";
	setAttr ".hpb" yes;
	setAttr ".do" 3;
createNode displayLayer -n "CONTROLLERS";
	rename -uid "5C79096F-4242-9C35-DC7B-5F8C1F94041F";
	setAttr ".hpb" yes;
	setAttr ".do" 4;
createNode condition -n "ctrl_L_F_Ankle_IK_conditionBalance_RF";
	rename -uid "20B2D38C-4EB8-8F12-5649-1DA88B415156";
	setAttr ".op" 2;
	setAttr ".cf" -type "float3" 0 0 1 ;
createNode condition -n "ctrl_L_F_Ankle_IK_conditionRoll_RF";
	rename -uid "3CE25C28-49FF-2156-CD83-EB840C09304C";
	setAttr ".op" 4;
	setAttr ".cf" -type "float3" 0 0 1 ;
createNode multiplyDivide -n "ctrl_L_F_Ankle_IK_Multiply_Compensate";
	rename -uid "484E9BC0-4BE5-C653-17F7-B5B97899C9B1";
createNode multiplyDivide -n "ctrl_L_F_Ankle_IK_Multiply_Reverse";
	rename -uid "38698C15-4695-8EB6-5AC6-DBA8FAEEE1B4";
	setAttr ".i2" -type "float3" -1 -1 1 ;
createNode blendColors -n "ctrl_L_F_Ankle_IK_bc_Weight";
	rename -uid "070B8A5D-4879-011C-FADB-19A9E59A51F4";
createNode multiplyDivide -n "L_F_UpperLeg_JNT_MultiplyDivide_Stretch";
	rename -uid "060092CD-4454-E008-C4A7-FDA07821AD8F";
	setAttr ".op" 2;
createNode blendColors -n "L_F_UpperLeg_JNT_bcTwist";
	rename -uid "0BDEC44A-4114-A7E4-806B-0280EC3FA122";
createNode clamp -n "L_F_UpperLeg_JNT_Clamp_Twist";
	rename -uid "39A222EE-4611-4923-3E5C-8F961A96D50A";
	setAttr ".mn" -type "float3" 1 0 0 ;
	setAttr ".mx" -type "float3" 999 0 0 ;
createNode condition -n "ctrl_L_F_Ankle_IK_conditionStretch";
	rename -uid "51C0F41D-4F22-D82C-38B8-58924AB67680";
	setAttr ".op" 2;
createNode condition -n "ctrl_L_B_Ankle_IK_conditionBalance_RF";
	rename -uid "6BCA3FC7-4323-9012-84DE-4FA88BD8131A";
	setAttr ".op" 2;
	setAttr ".cf" -type "float3" 0 0 1 ;
createNode condition -n "ctrl_L_B_Ankle_IK_conditionRoll_RF";
	rename -uid "3FFB058C-4031-4E92-4359-5C8066D4C217";
	setAttr ".op" 4;
	setAttr ".cf" -type "float3" 0 0 1 ;
createNode multiplyDivide -n "ctrl_L_B_Ankle_IK_Multiply_Compensate";
	rename -uid "D4901C09-41EB-AA8D-459B-C1BEBFAA183F";
createNode multiplyDivide -n "ctrl_L_B_Ankle_IK_Multiply_Reverse";
	rename -uid "60ADE3DA-49F5-5664-C33C-C19B2C70EA90";
	setAttr ".i2" -type "float3" -1 -1 1 ;
createNode blendColors -n "ctrl_L_B_Ankle_IK_bc_Weight";
	rename -uid "6C05896B-46AD-2C56-923B-F6A975043565";
createNode multiplyDivide -n "L_B_UpperLeg_JNT_MultiplyDivide_Stretch";
	rename -uid "3EBFFA67-4145-9FB6-7191-A1A8F209FDB3";
	setAttr ".op" 2;
createNode blendColors -n "L_B_UpperLeg_JNT_bcTwist";
	rename -uid "A19F9450-438B-2897-83C6-3EBEBB461799";
createNode clamp -n "L_B_UpperLeg_JNT_Clamp_Twist";
	rename -uid "0D04A8FA-4EAB-708B-33B3-64950E8043EA";
	setAttr ".mn" -type "float3" 1 0 0 ;
	setAttr ".mx" -type "float3" 999 0 0 ;
createNode condition -n "ctrl_L_B_Ankle_IK_conditionStretch";
	rename -uid "5B928533-49E8-E1AD-B7F7-0D88DC38BB81";
	setAttr ".op" 2;
createNode displayLayer -n "HELPERS";
	rename -uid "E1194902-47CC-5279-35F8-FF8CEEA95729";
	setAttr ".hpb" yes;
	setAttr ".do" 5;
createNode condition -n "ctrl_R_F_Ankle_IK_conditionBalance_RF";
	rename -uid "B6D99861-491D-891A-AA5A-A9AE1B594651";
	setAttr ".op" 2;
	setAttr ".cf" -type "float3" 0 0 1 ;
createNode condition -n "ctrl_R_F_Ankle_IK_conditionRoll_RF";
	rename -uid "438967A7-40D7-0C34-88DB-CD86ADE9C588";
	setAttr ".op" 4;
	setAttr ".cf" -type "float3" 0 0 1 ;
createNode multiplyDivide -n "ctrl_R_F_Ankle_IK_Multiply_Compensate";
	rename -uid "EF3ED8F1-48BE-445C-9B13-0C8530DA5E4A";
createNode multiplyDivide -n "ctrl_R_F_Ankle_IK_Multiply_Reverse";
	rename -uid "3BAD92B1-4BAD-0A5B-4051-3C9379AAFA0B";
	setAttr ".i2" -type "float3" -1 -1 1 ;
createNode blendColors -n "ctrl_R_F_Ankle_IK_bc_Weight";
	rename -uid "EC1C3FDB-413C-F3DD-F355-FE93706BC6F5";
createNode multiplyDivide -n "R_F_UpperLeg_JNT_MultiplyDivide_Stretch";
	rename -uid "E17C1BE2-4621-2F56-75F6-F8A45CD17C13";
	setAttr ".op" 2;
createNode blendColors -n "R_F_UpperLeg_JNT_bcTwist";
	rename -uid "11CD336B-413B-4A7A-517A-ED8B5DFC708C";
createNode clamp -n "R_F_UpperLeg_JNT_Clamp_Twist";
	rename -uid "2949665A-488E-126D-2D1C-ED9319A56FA9";
	setAttr ".mn" -type "float3" 1 0 0 ;
	setAttr ".mx" -type "float3" 999 0 0 ;
createNode condition -n "ctrl_R_F_Ankle_IK_conditionStretch";
	rename -uid "06DF2229-4DF3-A8F0-9D81-D4955F4EBCAA";
	setAttr ".op" 2;
createNode condition -n "ctrl_R_B_Ankle_IK_conditionBalance_RF";
	rename -uid "D1DC057F-4B14-2226-9248-A09C853ED5F8";
	setAttr ".op" 2;
	setAttr ".cf" -type "float3" 0 0 1 ;
createNode condition -n "ctrl_R_B_Ankle_IK_conditionRoll_RF";
	rename -uid "FE626A22-4180-CE68-D9E1-B9903371EF05";
	setAttr ".op" 4;
	setAttr ".cf" -type "float3" 0 0 1 ;
createNode multiplyDivide -n "ctrl_R_B_Ankle_IK_Multiply_Compensate";
	rename -uid "1851F787-46B7-3C50-9C64-6587CA176C18";
createNode multiplyDivide -n "ctrl_R_B_Ankle_IK_Multiply_Reverse";
	rename -uid "A023C14C-4EB4-5971-C7FA-E5BECB2505D0";
	setAttr ".i2" -type "float3" -1 -1 1 ;
createNode blendColors -n "ctrl_R_B_Ankle_IK_bc_Weight";
	rename -uid "0EF87FBC-419E-93FC-4B90-D69BD086423A";
createNode multiplyDivide -n "R_B_UpperLeg_JNT_MultiplyDivide_Stretch";
	rename -uid "B628F03D-4236-2C0D-7FDA-2DAF96A1B905";
	setAttr ".op" 2;
createNode blendColors -n "R_B_UpperLeg_JNT_bcTwist";
	rename -uid "5C986E9C-4C68-85C8-B430-279A9B7857B2";
createNode clamp -n "R_B_UpperLeg_JNT_Clamp_Twist";
	rename -uid "3C4194DD-457A-4C5B-D5E4-FFA959EF1853";
	setAttr ".mn" -type "float3" 1 0 0 ;
	setAttr ".mx" -type "float3" 999 0 0 ;
createNode condition -n "ctrl_R_B_Ankle_IK_conditionStretch";
	rename -uid "04387D93-4F64-26A5-F3A3-36B6F62825DE";
	setAttr ".op" 2;
createNode multiplyDivide -n "multiplyDivide1";
	rename -uid "FC7A9C7B-48E5-4DD3-B4EC-4CB90CE079E6";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
createNode multiplyDivide -n "multiplyDivide2";
	rename -uid "B0D674A0-4DB8-4B0D-9388-63A4EE5F6CCA";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
createNode multiplyDivide -n "multiplyDivide3";
	rename -uid "97C425BB-4A21-FEAA-3660-5BAE388FCEFD";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
createNode multiplyDivide -n "multiplyDivide4";
	rename -uid "1F8DB5B2-4630-8B2B-0FE0-D59DD9D73BFC";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
createNode multiplyDivide -n "_MultiplyDivide_RibbonStretch";
	rename -uid "3547C345-40AD-87DD-9DFA-61AF7B90AD21";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 41.599998 1 1 ;
createNode blendColors -n "_bcRibbon";
	rename -uid "52307023-4AE9-FE1C-F174-1B8F8A42EDFA";
createNode clamp -n "_ClampRibbon";
	rename -uid "8BD1E539-44BE-D2DF-5889-7B8F78701CBE";
	setAttr ".mn" -type "float3" 1 0 0 ;
	setAttr ".mx" -type "float3" 999 0 0 ;
createNode multiplyDivide -n "_MultiplyDivide_RibbonStretch2";
	rename -uid "CE1420F8-49F3-5289-E7C4-3DBDEF7ACC56";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
createNode multiplyDivide -n "NeckRibbon__MultiplyDivide_RibbonStretch";
	rename -uid "8EA11E5F-4E8C-B3B1-622B-35A431BDA086";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 46.222225 1 1 ;
createNode blendColors -n "NeckRibbon__bcRibbon";
	rename -uid "52C252E6-4A92-AB78-28E0-01AFAE425A5F";
createNode clamp -n "NeckRibbon__ClampRibbon";
	rename -uid "32727C49-4191-6C84-11B6-299FF40B3DD0";
	setAttr ".mn" -type "float3" 1 0 0 ;
	setAttr ".mx" -type "float3" 999 0 0 ;
createNode multiplyDivide -n "NeckRibbon__MultiplyDivide_RibbonStretch2";
	rename -uid "D66C2D3A-4CFF-EA20-523B-43A8419C425E";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 0 0 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "8C4B18B7-48AC-F652-D562-3381492430AF";
	setAttr -s 8 ".tgi";
	setAttr ".tgi[0].tn" -type "string" "Untitled_4";
	setAttr ".tgi[0].vl" -type "double2" -773.9926432369698 -383.3333181010359 ;
	setAttr ".tgi[0].vh" -type "double2" 2021.6116412800927 373.80950895566849 ;
	setAttr -s 21 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" -220;
	setAttr ".tgi[0].ni[0].y" -125.71428680419922;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 246.78074645996094;
	setAttr ".tgi[0].ni[1].y" 171.62666320800781;
	setAttr ".tgi[0].ni[1].nvs" 18306;
	setAttr ".tgi[0].ni[2].x" -1107.142822265625;
	setAttr ".tgi[0].ni[2].y" -427.14285278320313;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 570.22900390625;
	setAttr ".tgi[0].ni[3].y" 439.5458984375;
	setAttr ".tgi[0].ni[3].nvs" 18306;
	setAttr ".tgi[0].ni[4].x" 295.71429443359375;
	setAttr ".tgi[0].ni[4].y" -528.5714111328125;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" 902.85711669921875;
	setAttr ".tgi[0].ni[5].y" -388.57144165039063;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" 288.57144165039063;
	setAttr ".tgi[0].ni[6].y" -338.57144165039063;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" -1544.2857666015625;
	setAttr ".tgi[0].ni[7].y" -308.57144165039063;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" -1544.2857666015625;
	setAttr ".tgi[0].ni[8].y" -410;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" 281.42855834960938;
	setAttr ".tgi[0].ni[9].y" -528.5714111328125;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" -702.85711669921875;
	setAttr ".tgi[0].ni[10].y" -370;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" -205.71427917480469;
	setAttr ".tgi[0].ni[11].y" -125.71428680419922;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" 848.90802001953125;
	setAttr ".tgi[0].ni[12].y" 302.78512573242188;
	setAttr ".tgi[0].ni[12].nvs" 18306;
	setAttr ".tgi[0].ni[13].x" 595.71429443359375;
	setAttr ".tgi[0].ni[13].y" 38.571430206298828;
	setAttr ".tgi[0].ni[13].nvs" 18306;
	setAttr ".tgi[0].ni[14].x" -352.85714721679688;
	setAttr ".tgi[0].ni[14].y" -392.85714721679688;
	setAttr ".tgi[0].ni[14].nvs" 18304;
	setAttr ".tgi[0].ni[15].x" 48.571430206298828;
	setAttr ".tgi[0].ni[15].y" -125.71428680419922;
	setAttr ".tgi[0].ni[15].nvs" 18304;
	setAttr ".tgi[0].ni[16].x" -1530;
	setAttr ".tgi[0].ni[16].y" -360;
	setAttr ".tgi[0].ni[16].nvs" 18304;
	setAttr ".tgi[0].ni[17].x" -45.714286804199219;
	setAttr ".tgi[0].ni[17].y" -364.28570556640625;
	setAttr ".tgi[0].ni[17].nvs" 18306;
	setAttr ".tgi[0].ni[18].x" 595.71429443359375;
	setAttr ".tgi[0].ni[18].y" -567.14288330078125;
	setAttr ".tgi[0].ni[18].nvs" 18304;
	setAttr ".tgi[0].ni[19].x" 14.285714149475098;
	setAttr ".tgi[0].ni[19].y" -125.71428680419922;
	setAttr ".tgi[0].ni[19].nvs" 18304;
	setAttr ".tgi[0].ni[20].x" -1530;
	setAttr ".tgi[0].ni[20].y" -461.42855834960938;
	setAttr ".tgi[0].ni[20].nvs" 18304;
	setAttr ".tgi[1].tn" -type "string" "Untitled_5";
	setAttr ".tgi[1].vl" -type "double2" -463.73624530904459 -17.85714214756565 ;
	setAttr ".tgi[1].vh" -type "double2" 2749.4504401972017 852.38091851037609 ;
	setAttr -s 15 ".tgi[1].ni";
	setAttr ".tgi[1].ni[0].x" -1394.2857666015625;
	setAttr ".tgi[1].ni[0].y" 21.428571701049805;
	setAttr ".tgi[1].ni[0].nvs" 18304;
	setAttr ".tgi[1].ni[1].x" 444.28570556640625;
	setAttr ".tgi[1].ni[1].y" -184.28572082519531;
	setAttr ".tgi[1].ni[1].nvs" 18304;
	setAttr ".tgi[1].ni[2].x" -1394.2857666015625;
	setAttr ".tgi[1].ni[2].y" 122.85713958740234;
	setAttr ".tgi[1].ni[2].nvs" 18304;
	setAttr ".tgi[1].ni[3].x" 1386.8424072265625;
	setAttr ".tgi[1].ni[3].y" 800.99261474609375;
	setAttr ".tgi[1].ni[3].nvs" 18306;
	setAttr ".tgi[1].ni[4].x" -955.71429443359375;
	setAttr ".tgi[1].ni[4].y" 42.857143402099609;
	setAttr ".tgi[1].ni[4].nvs" 18304;
	setAttr ".tgi[1].ni[5].x" 1058.5714111328125;
	setAttr ".tgi[1].ni[5].y" -115.71428680419922;
	setAttr ".tgi[1].ni[5].nvs" 18304;
	setAttr ".tgi[1].ni[6].x" -550;
	setAttr ".tgi[1].ni[6].y" 10;
	setAttr ".tgi[1].ni[6].nvs" 18304;
	setAttr ".tgi[1].ni[7].x" 1163.8499755859375;
	setAttr ".tgi[1].ni[7].y" 508.84194946289063;
	setAttr ".tgi[1].ni[7].nvs" 18306;
	setAttr ".tgi[1].ni[8].x" -198.57142639160156;
	setAttr ".tgi[1].ni[8].y" -37.142856597900391;
	setAttr ".tgi[1].ni[8].nvs" 18304;
	setAttr ".tgi[1].ni[9].x" 610.38885498046875;
	setAttr ".tgi[1].ni[9].y" 665.7083740234375;
	setAttr ".tgi[1].ni[9].nvs" 18306;
	setAttr ".tgi[1].ni[10].x" -1380;
	setAttr ".tgi[1].ni[10].y" -42.857143402099609;
	setAttr ".tgi[1].ni[10].nvs" 18304;
	setAttr ".tgi[1].ni[11].x" 116.28778839111328;
	setAttr ".tgi[1].ni[11].y" -14.852302551269531;
	setAttr ".tgi[1].ni[11].nvs" 18305;
	setAttr ".tgi[1].ni[12].x" 751.4285888671875;
	setAttr ".tgi[1].ni[12].y" -285.71429443359375;
	setAttr ".tgi[1].ni[12].nvs" 18304;
	setAttr ".tgi[1].ni[13].x" -1380;
	setAttr ".tgi[1].ni[13].y" 71.428573608398438;
	setAttr ".tgi[1].ni[13].nvs" 18304;
	setAttr ".tgi[1].ni[14].x" 751.4285888671875;
	setAttr ".tgi[1].ni[14].y" 320;
	setAttr ".tgi[1].ni[14].nvs" 18306;
	setAttr ".tgi[2].tn" -type "string" "Untitled_6";
	setAttr ".tgi[2].vl" -type "double2" 301.46518948605103 -302.38094036541338 ;
	setAttr ".tgi[2].vh" -type "double2" 4850.9155581576852 929.76186781648755 ;
	setAttr -s 21 ".tgi[2].ni";
	setAttr ".tgi[2].ni[0].x" 761.4285888671875;
	setAttr ".tgi[2].ni[0].y" -312.85714721679688;
	setAttr ".tgi[2].ni[0].nvs" 18304;
	setAttr ".tgi[2].ni[1].x" 337.14285278320313;
	setAttr ".tgi[2].ni[1].y" -347.14285278320313;
	setAttr ".tgi[2].ni[1].nvs" 18304;
	setAttr ".tgi[2].ni[2].x" 2164.28564453125;
	setAttr ".tgi[2].ni[2].y" -124.28571319580078;
	setAttr ".tgi[2].ni[2].nvs" 18304;
	setAttr ".tgi[2].ni[3].x" 1520;
	setAttr ".tgi[2].ni[3].y" -280;
	setAttr ".tgi[2].ni[3].nvs" 18304;
	setAttr ".tgi[2].ni[4].x" 1167.142822265625;
	setAttr ".tgi[2].ni[4].y" -257.14285278320313;
	setAttr ".tgi[2].ni[4].nvs" 18304;
	setAttr ".tgi[2].ni[5].x" 322.85714721679688;
	setAttr ".tgi[2].ni[5].y" -195.71427917480469;
	setAttr ".tgi[2].ni[5].nvs" 18304;
	setAttr ".tgi[2].ni[6].x" 2841.003173828125;
	setAttr ".tgi[2].ni[6].y" 768.0582275390625;
	setAttr ".tgi[2].ni[6].nvs" 18306;
	setAttr ".tgi[2].ni[7].x" 1958.5714111328125;
	setAttr ".tgi[2].ni[7].y" 625.71429443359375;
	setAttr ".tgi[2].ni[7].nvs" 18304;
	setAttr ".tgi[2].ni[8].x" 3525.71435546875;
	setAttr ".tgi[2].ni[8].y" 345.71429443359375;
	setAttr ".tgi[2].ni[8].nvs" 18304;
	setAttr ".tgi[2].ni[9].x" 1966.505126953125;
	setAttr ".tgi[2].ni[9].y" 253.54649353027344;
	setAttr ".tgi[2].ni[9].nvs" 18482;
	setAttr ".tgi[2].ni[10].x" 322.85714721679688;
	setAttr ".tgi[2].ni[10].y" -297.14285278320313;
	setAttr ".tgi[2].ni[10].nvs" 18304;
	setAttr ".tgi[2].ni[11].x" 1437.142822265625;
	setAttr ".tgi[2].ni[11].y" 345.71429443359375;
	setAttr ".tgi[2].ni[11].nvs" 18304;
	setAttr ".tgi[2].ni[12].x" 2471.428466796875;
	setAttr ".tgi[2].ni[12].y" -454.28570556640625;
	setAttr ".tgi[2].ni[12].nvs" 18304;
	setAttr ".tgi[2].ni[13].x" 3073.8134765625;
	setAttr ".tgi[2].ni[13].y" 494.05633544921875;
	setAttr ".tgi[2].ni[13].nvs" 18306;
	setAttr ".tgi[2].ni[14].x" 2480;
	setAttr ".tgi[2].ni[14].y" 575.71429443359375;
	setAttr ".tgi[2].ni[14].nvs" 18304;
	setAttr ".tgi[2].ni[15].x" 2465.71435546875;
	setAttr ".tgi[2].ni[15].y" 575.71429443359375;
	setAttr ".tgi[2].ni[15].nvs" 18304;
	setAttr ".tgi[2].ni[16].x" 1827.142822265625;
	setAttr ".tgi[2].ni[16].y" -251.42857360839844;
	setAttr ".tgi[2].ni[16].nvs" 18306;
	setAttr ".tgi[2].ni[17].x" 337.14285278320313;
	setAttr ".tgi[2].ni[17].y" -245.71427917480469;
	setAttr ".tgi[2].ni[17].nvs" 18304;
	setAttr ".tgi[2].ni[18].x" 2778.571533203125;
	setAttr ".tgi[2].ni[18].y" -275.71429443359375;
	setAttr ".tgi[2].ni[18].nvs" 18304;
	setAttr ".tgi[2].ni[19].x" 1944.2857666015625;
	setAttr ".tgi[2].ni[19].y" 625.71429443359375;
	setAttr ".tgi[2].ni[19].nvs" 18304;
	setAttr ".tgi[2].ni[20].x" 2471.428466796875;
	setAttr ".tgi[2].ni[20].y" 151.42857360839844;
	setAttr ".tgi[2].ni[20].nvs" 18306;
	setAttr ".tgi[3].tn" -type "string" "Untitled_7";
	setAttr ".tgi[3].vl" -type "double2" -1873.9468119829307 -363.09522366712895 ;
	setAttr ".tgi[3].vh" -type "double2" 2679.8991609096429 870.23806065794304 ;
	setAttr -s 15 ".tgi[3].ni";
	setAttr ".tgi[3].ni[0].x" 1212.55859375;
	setAttr ".tgi[3].ni[0].y" 569.8646240234375;
	setAttr ".tgi[3].ni[0].nvs" 18306;
	setAttr ".tgi[3].ni[1].x" 1435.1654052734375;
	setAttr ".tgi[3].ni[1].y" 916.99749755859375;
	setAttr ".tgi[3].ni[1].nvs" 18306;
	setAttr ".tgi[3].ni[2].x" 801.4285888671875;
	setAttr ".tgi[3].ni[2].y" -264.28570556640625;
	setAttr ".tgi[3].ni[2].nvs" 18304;
	setAttr ".tgi[3].ni[3].x" -1351.4285888671875;
	setAttr ".tgi[3].ni[3].y" -5.7142858505249023;
	setAttr ".tgi[3].ni[3].nvs" 18304;
	setAttr ".tgi[3].ni[4].x" -151.42857360839844;
	setAttr ".tgi[3].ni[4].y" -90;
	setAttr ".tgi[3].ni[4].nvs" 18304;
	setAttr ".tgi[3].ni[5].x" -1337.142822265625;
	setAttr ".tgi[3].ni[5].y" -57.142856597900391;
	setAttr ".tgi[3].ni[5].nvs" 18304;
	setAttr ".tgi[3].ni[6].x" 1108.5714111328125;
	setAttr ".tgi[3].ni[6].y" -85.714286804199219;
	setAttr ".tgi[3].ni[6].nvs" 18304;
	setAttr ".tgi[3].ni[7].x" 801.4285888671875;
	setAttr ".tgi[3].ni[7].y" 341.42855834960938;
	setAttr ".tgi[3].ni[7].nvs" 18306;
	setAttr ".tgi[3].ni[8].x" 155.71427917480469;
	setAttr ".tgi[3].ni[8].y" -61.428569793701172;
	setAttr ".tgi[3].ni[8].nvs" 18306;
	setAttr ".tgi[3].ni[9].x" -504.28570556640625;
	setAttr ".tgi[3].ni[9].y" -67.142860412597656;
	setAttr ".tgi[3].ni[9].nvs" 18304;
	setAttr ".tgi[3].ni[10].x" 481.51318359375;
	setAttr ".tgi[3].ni[10].y" -223.65283203125;
	setAttr ".tgi[3].ni[10].nvs" 18304;
	setAttr ".tgi[3].ni[11].x" -1351.4285888671875;
	setAttr ".tgi[3].ni[11].y" -107.14286041259766;
	setAttr ".tgi[3].ni[11].nvs" 18304;
	setAttr ".tgi[3].ni[12].x" -911.4285888671875;
	setAttr ".tgi[3].ni[12].y" -124.28571319580078;
	setAttr ".tgi[3].ni[12].nvs" 18304;
	setAttr ".tgi[3].ni[13].x" -1337.142822265625;
	setAttr ".tgi[3].ni[13].y" -158.57142639160156;
	setAttr ".tgi[3].ni[13].nvs" 18304;
	setAttr ".tgi[3].ni[14].x" 530.975830078125;
	setAttr ".tgi[3].ni[14].y" 626.06878662109375;
	setAttr ".tgi[3].ni[14].nvs" 18306;
	setAttr ".tgi[4].tn" -type "string" "Untitled_8";
	setAttr ".tgi[4].vl" -type "double2" -974.40472318539696 -185.71427833466333 ;
	setAttr ".tgi[4].vh" -type "double2" 1311.309471702767 433.33331611421443 ;
	setAttr -s 8 ".tgi[4].ni";
	setAttr ".tgi[4].ni[0].x" -316.38653564453125;
	setAttr ".tgi[4].ni[0].y" 356.38653564453125;
	setAttr ".tgi[4].ni[0].nvs" 18306;
	setAttr ".tgi[4].ni[1].x" 94.863243103027344;
	setAttr ".tgi[4].ni[1].y" 376.24609375;
	setAttr ".tgi[4].ni[1].nvs" 18306;
	setAttr ".tgi[4].ni[2].x" -230;
	setAttr ".tgi[4].ni[2].y" 430;
	setAttr ".tgi[4].ni[2].nvs" 18304;
	setAttr ".tgi[4].ni[3].x" 87.142860412597656;
	setAttr ".tgi[4].ni[3].y" -75.714286804199219;
	setAttr ".tgi[4].ni[3].nvs" 18304;
	setAttr ".tgi[4].ni[4].x" 431.76968383789063;
	setAttr ".tgi[4].ni[4].y" 497.40866088867188;
	setAttr ".tgi[4].ni[4].nvs" 18306;
	setAttr ".tgi[4].ni[5].x" 27.142856597900391;
	setAttr ".tgi[4].ni[5].y" 25.714284896850586;
	setAttr ".tgi[4].ni[5].nvs" 18304;
	setAttr ".tgi[4].ni[6].x" -354.28570556640625;
	setAttr ".tgi[4].ni[6].y" 430;
	setAttr ".tgi[4].ni[6].nvs" 18304;
	setAttr ".tgi[4].ni[7].x" 71.428573608398438;
	setAttr ".tgi[4].ni[7].y" 25.714284896850586;
	setAttr ".tgi[4].ni[7].nvs" 18304;
	setAttr ".tgi[5].tn" -type "string" "Untitled_9";
	setAttr ".tgi[5].vl" -type "double2" -479.76188569788025 -435.71426840055625 ;
	setAttr ".tgi[5].vh" -type "double2" 744.04758948182439 196.4285636232016 ;
	setAttr -s 3 ".tgi[5].ni";
	setAttr ".tgi[5].ni[0].x" 346.84600830078125;
	setAttr ".tgi[5].ni[0].y" 229.92408752441406;
	setAttr ".tgi[5].ni[0].nvs" 18306;
	setAttr ".tgi[5].ni[1].x" 23.737524032592773;
	setAttr ".tgi[5].ni[1].y" 212.88905334472656;
	setAttr ".tgi[5].ni[1].nvs" 18306;
	setAttr ".tgi[5].ni[2].x" -347.14285278320313;
	setAttr ".tgi[5].ni[2].y" 189.41175842285156;
	setAttr ".tgi[5].ni[2].nvs" 18306;
	setAttr ".tgi[6].tn" -type "string" "Untitled_10";
	setAttr ".tgi[6].vl" -type "double2" -427.64768261838577 -557.76239206176194 ;
	setAttr ".tgi[6].vh" -type "double2" 794.0426546431496 73.285826893369531 ;
	setAttr -s 8 ".tgi[6].ni";
	setAttr ".tgi[6].ni[0].x" 421.00839233398438;
	setAttr ".tgi[6].ni[0].y" 205.96638488769531;
	setAttr ".tgi[6].ni[0].nvs" 18306;
	setAttr ".tgi[6].ni[1].x" -48.774509429931641;
	setAttr ".tgi[6].ni[1].y" 136.8697509765625;
	setAttr ".tgi[6].ni[1].nvs" 18306;
	setAttr ".tgi[6].ni[2].x" -334.45376586914063;
	setAttr ".tgi[6].ni[2].y" 159.41175842285156;
	setAttr ".tgi[6].ni[2].nvs" 18306;
	setAttr ".tgi[6].ni[3].x" 37.142856597900391;
	setAttr ".tgi[6].ni[3].y" -325.71429443359375;
	setAttr ".tgi[6].ni[3].nvs" 18304;
	setAttr ".tgi[6].ni[4].x" 125.71428680419922;
	setAttr ".tgi[6].ni[4].y" -452.85714721679688;
	setAttr ".tgi[6].ni[4].nvs" 18304;
	setAttr ".tgi[6].ni[5].x" 7.1428570747375488;
	setAttr ".tgi[6].ni[5].y" -224.28572082519531;
	setAttr ".tgi[6].ni[5].nvs" 18304;
	setAttr ".tgi[6].ni[6].x" 81.428573608398438;
	setAttr ".tgi[6].ni[6].y" -224.28572082519531;
	setAttr ".tgi[6].ni[6].nvs" 18304;
	setAttr ".tgi[6].ni[7].x" 51.428569793701172;
	setAttr ".tgi[6].ni[7].y" -452.85714721679688;
	setAttr ".tgi[6].ni[7].nvs" 18304;
	setAttr ".tgi[7].tn" -type "string" "Untitled_11";
	setAttr ".tgi[7].vl" -type "double2" -497.1941663027107 -449.13639908871835 ;
	setAttr ".tgi[7].vh" -type "double2" 724.49617095882479 271.0429242386071 ;
	setAttr -s 3 ".tgi[7].ni";
	setAttr ".tgi[7].ni[0].x" 241.73867797851563;
	setAttr ".tgi[7].ni[0].y" 223.08195495605469;
	setAttr ".tgi[7].ni[0].nvs" 18306;
	setAttr ".tgi[7].ni[1].x" -306.72268676757813;
	setAttr ".tgi[7].ni[1].y" 222.43696594238281;
	setAttr ".tgi[7].ni[1].nvs" 18306;
	setAttr ".tgi[7].ni[2].x" -30.147178649902344;
	setAttr ".tgi[7].ni[2].y" 218.75267028808594;
	setAttr ".tgi[7].ni[2].nvs" 18306;
createNode phong -n "_Fire_Adult_LEFT_LEGS___Copy_A_Fire";
	rename -uid "F5B4F26F-40E1-220B-80CA-F4B3F77D9043";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG";
	rename -uid "AFB648F1-49CA-E4EF-62A1-96B26A492076";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "_Fire_Adult_LEFT_LEGS___Copy_materialInfo1";
	rename -uid "B3BEAE62-48C6-B110-FB8D-9C897BBF5BD5";
createNode file -n "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037";
	rename -uid "5EFD4D91-49D0-5CCF-6597-838DC3530BC8";
	setAttr ".ftn" -type "string" "D:/SOCIAL_POINT/DragonCity2/ExternalResources/Fire_Adult/TEX_CHR_A_Fire_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1";
	rename -uid "DA8A9079-4CF9-1EDB-946D-F6BC8E41BF7F";
createNode phong -n "_Fire_Adult_LEFT_LEGS___Copy_A_Fire1";
	rename -uid "35D986D0-49CC-3489-7786-4A80D14823E7";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG1";
	rename -uid "7B3A9CCD-4ABC-FB75-4797-71BC4B73A6B2";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "_Fire_Adult_LEFT_LEGS___Copy_materialInfo2";
	rename -uid "98B51055-4F45-C31B-8976-2DAC70AEE4D9";
createNode file -n "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038";
	rename -uid "23127CDE-4BB1-B0F4-F802-A9B91B019769";
	setAttr ".ftn" -type "string" "D:/SOCIAL_POINT/DragonCity2/ExternalResources/DragonsRef/Textures/TEX_CHR_A_Fire_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2";
	rename -uid "6C0DF722-4190-E2F6-1E76-63BB8ACC1B32";
createNode phong -n "_Fire_Adult_BLENDSHADES1:A_Fire";
	rename -uid "D2A3DBFE-49CF-3788-9D12-54B9E2D992E8";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "_Fire_Adult_BLENDSHADES1:Flame_AdultSG";
	rename -uid "84BB0E8C-4B9B-FBE8-647B-3CBDC999C696";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "_Fire_Adult_BLENDSHADES1:materialInfo1";
	rename -uid "B50E5885-40DF-935C-ABA1-F9844350FE57";
createNode file -n "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037";
	rename -uid "6072D5D3-4740-263E-C688-3C8523848276";
	setAttr ".ftn" -type "string" "D:/SOCIAL_POINT/DragonCity2/ExternalResources/Fire_Adult/TEX_CHR_A_Fire_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "_Fire_Adult_BLENDSHADES1:place2dTexture1";
	rename -uid "80AF59DF-4BFC-381C-2A2D-228209A42191";
createNode phong -n "_Fire_Adult_BLENDSHADES1:A_Fire1";
	rename -uid "F9D78E83-4E07-7729-C914-6CAA460F63BF";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "_Fire_Adult_BLENDSHADES1:Flame_AdultSG1";
	rename -uid "1BF3E464-4B65-204C-D726-708E9DB76C94";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "_Fire_Adult_BLENDSHADES1:materialInfo2";
	rename -uid "E81F4F1D-4447-C538-835B-88935F824643";
createNode file -n "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038";
	rename -uid "F59990F2-4DA8-B567-CA64-C0850329CD38";
	setAttr ".ftn" -type "string" "D:/SOCIAL_POINT/DragonCity2/ExternalResources/DragonsRef/Textures/TEX_CHR_A_Fire_D.png";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "_Fire_Adult_BLENDSHADES1:place2dTexture2";
	rename -uid "A2EECC92-4895-9BC3-8ECE-8AA27C220A58";
createNode phong -n "Knight_A_ncl1_1";
	rename -uid "645C36F7-4E6E-26C2-4065-CE80835CCC9D";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "L_Eye_OpenSG";
	rename -uid "A7D76D4B-41E7-C60A-4E2E-E4BFFEBED451";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo3";
	rename -uid "D27457CB-4B7A-AEEB-0420-90BCAA4BC356";
createNode file -n "MapFBXASC032FBXASC0352";
	rename -uid "2303ACA6-408D-24FF-6775-479037BEACB7";
	setAttr ".ftn" -type "string" "E:\\HDD_DATA\\SOCIAL_POINT\\DragonCity2\\ExternalResources\\Matrix\\Textures\\TEX_CHR_Knight_A_D.jpg";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture3";
	rename -uid "616DECA5-4D08-4E2A-4A71-E387A04BA782";
createNode phong -n "Knight_A_ncl1_2";
	rename -uid "D1A1EDAD-496F-99CA-E64A-CEBC3C22C1A0";
	setAttr ".dc" 1;
	setAttr ".ambc" -type "float3" 0.588 0.588 0.588 ;
	setAttr ".sc" -type "float3" 0 0 0 ;
	setAttr ".rfl" 1;
	setAttr ".cp" 2;
createNode shadingEngine -n "L_Eye_OpenSG1";
	rename -uid "9B580B8F-406E-3831-F0B8-8C96E36EDD6E";
	setAttr ".ihi" 0;
	setAttr ".ro" yes;
createNode materialInfo -n "materialInfo4";
	rename -uid "4B5A86DF-4FA5-5FE1-9636-F7B1CC7D5848";
createNode file -n "MapFBXASC032FBXASC0353";
	rename -uid "25F04C85-4EEF-0DC3-3014-92A1BCB71140";
	setAttr ".ftn" -type "string" "E:\\HDD_DATA\\SOCIAL_POINT\\DragonCity2\\ExternalResources\\Matrix\\Textures\\TEX_CHR_Knight_A_D.jpg";
	setAttr ".cs" -type "string" "sRGB";
createNode place2dTexture -n "place2dTexture4";
	rename -uid "B8BB1174-4F27-3316-E016-3A8F64989943";
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 0;
	setAttr -av -k on ".unw";
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr -av -k on ".ihi";
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr -av ".ta";
	setAttr -av ".tq";
	setAttr -av ".aoam";
	setAttr -av ".aora";
	setAttr -av ".hfd";
	setAttr -av ".hfe";
	setAttr -av ".hfa";
	setAttr -av ".mbe";
	setAttr -av -k on ".mbsof";
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 12 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 14 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 58 ".u";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
select -ne :defaultTextureList1;
	setAttr -cb on ".cch";
	setAttr -cb on ".ihi";
	setAttr -cb on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 10 ".tx";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -av -cb on ".macc";
	setAttr -av -cb on ".macd";
	setAttr -av -cb on ".macq";
	setAttr -av -k on ".mcfr" 60;
	setAttr -cb on ".ifg";
	setAttr -av -k on ".clip";
	setAttr -av -k on ".edm";
	setAttr -av -k on ".edl";
	setAttr -k on ".ren";
	setAttr -av -k on ".esr";
	setAttr -av -k on ".ors";
	setAttr -cb on ".sdf";
	setAttr -av -k on ".outf";
	setAttr -av -cb on ".imfkey";
	setAttr -av -k on ".gama";
	setAttr -av -cb on ".an";
	setAttr -cb on ".ar";
	setAttr -k on ".fs";
	setAttr -k on ".ef";
	setAttr -av -k on ".bfs";
	setAttr -cb on ".me";
	setAttr -cb on ".se";
	setAttr -av -k on ".be";
	setAttr -av -cb on ".ep";
	setAttr -av -k on ".fec";
	setAttr -av -k on ".ofc";
	setAttr -cb on ".ofe";
	setAttr -cb on ".efe";
	setAttr -cb on ".oft";
	setAttr -cb on ".umfn";
	setAttr -cb on ".ufe";
	setAttr -av -cb on ".pff";
	setAttr -av -cb on ".peie";
	setAttr -av -cb on ".ifp";
	setAttr -k on ".rv";
	setAttr -av -k on ".comp";
	setAttr -av -k on ".cth";
	setAttr -av -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -av -k on ".rd";
	setAttr -av -k on ".lp";
	setAttr -av -k on ".sp";
	setAttr -av -k on ".shs";
	setAttr -av -k on ".lpr";
	setAttr -cb on ".gv";
	setAttr -cb on ".sv";
	setAttr -av -k on ".mm";
	setAttr -av -k on ".npu";
	setAttr -av -k on ".itf";
	setAttr -av -k on ".shp";
	setAttr -cb on ".isp";
	setAttr -av -k on ".uf";
	setAttr -av -k on ".oi";
	setAttr -av -k on ".rut";
	setAttr -av -k on ".mot";
	setAttr -av -k on ".mb";
	setAttr -av -k on ".mbf";
	setAttr -av -k on ".mbso";
	setAttr -av -k on ".mbsc";
	setAttr -av -k on ".afp";
	setAttr -av -k on ".pfb";
	setAttr -k on ".pram";
	setAttr -k on ".poam";
	setAttr -k on ".prlm";
	setAttr -k on ".polm";
	setAttr -cb on ".prm";
	setAttr -cb on ".pom";
	setAttr -cb on ".pfrm";
	setAttr -cb on ".pfom";
	setAttr -av -k on ".bll";
	setAttr -av -k on ".bls";
	setAttr -av -k on ".smv";
	setAttr -av -k on ".ubc";
	setAttr -av -k on ".mbc";
	setAttr -cb on ".mbt";
	setAttr -av -k on ".udbx";
	setAttr -av -k on ".smc";
	setAttr -av -k on ".kmv";
	setAttr -cb on ".isl";
	setAttr -cb on ".ism";
	setAttr -cb on ".imb";
	setAttr -av -k on ".rlen";
	setAttr -av -k on ".frts";
	setAttr -av -k on ".tlwd";
	setAttr -av -k on ".tlht";
	setAttr -av -k on ".jfc";
	setAttr -cb on ".rsb";
	setAttr -av -cb on ".ope";
	setAttr -av -cb on ".oppf";
	setAttr -av -k on ".rcp";
	setAttr -av -k on ".icp";
	setAttr -av -k on ".ocp";
	setAttr -cb on ".hbl";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr -av -k on ".cch";
	setAttr -av -k on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -k on ".bnm";
	setAttr -av -k on ".w";
	setAttr -av -k on ".h";
	setAttr -av -k on ".pa" 1;
	setAttr -av -k on ".al";
	setAttr -av -k on ".dar";
	setAttr -av -k on ".ldar";
	setAttr -av -k on ".dpi";
	setAttr -av -k on ".off";
	setAttr -av -k on ".fld";
	setAttr -av -k on ".zsl";
	setAttr -av -k on ".isu";
	setAttr -av -k on ".pdu";
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k off -cb on ".ctrs" 256;
	setAttr -av -k off -cb on ".btrs" 512;
	setAttr -k off -cb on ".fbfm";
	setAttr -k off -cb on ".ehql";
	setAttr -k off -cb on ".eams";
	setAttr -k off -cb on ".eeaa";
	setAttr -k off -cb on ".engm";
	setAttr -k off -cb on ".mes";
	setAttr -k off -cb on ".emb";
	setAttr -av -k off -cb on ".mbbf";
	setAttr -k off -cb on ".mbs";
	setAttr -k off -cb on ".trm";
	setAttr -k off -cb on ".tshc";
	setAttr -k off -cb on ".enpt";
	setAttr -k off -cb on ".clmt";
	setAttr -k off -cb on ".tcov";
	setAttr -k off -cb on ".lith";
	setAttr -k off -cb on ".sobc";
	setAttr -k off -cb on ".cuth";
	setAttr -k off -cb on ".hgcd";
	setAttr -k off -cb on ".hgci";
	setAttr -k off -cb on ".mgcs";
	setAttr -k off -cb on ".twa";
	setAttr -k off -cb on ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
	setAttr -k on ".hwfr" 60;
	setAttr -k on ".soll";
	setAttr -k on ".sosl";
	setAttr -k on ".bswa";
	setAttr -k on ".shml";
	setAttr -k on ".hwel";
connectAttr "JOINTS_REF.di" "JointsReference.do";
connectAttr "CONTROLLERS.di" "Controllers.do";
connectAttr "CONTROLLERS.di" "CTRL__Master.do";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Flame_AdultSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "Flame_AdultSG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "_Fire_Adult_BLENDSHADES:Flame_AdultSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "_Fire_Adult_BLENDSHADES:Flame_AdultSG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "_Fire_Adult_BLENDSHADES1:Flame_AdultSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "_Fire_Adult_BLENDSHADES1:Flame_AdultSG1.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "L_Eye_OpenSG.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" "L_Eye_OpenSG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Flame_AdultSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "Flame_AdultSG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "_Fire_Adult_BLENDSHADES:Flame_AdultSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "_Fire_Adult_BLENDSHADES:Flame_AdultSG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "_Fire_Adult_BLENDSHADES1:Flame_AdultSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "_Fire_Adult_BLENDSHADES1:Flame_AdultSG1.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "L_Eye_OpenSG.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" "L_Eye_OpenSG1.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.oc" "A_Fire.c";
connectAttr "A_Fire.oc" "Flame_AdultSG.ss";
connectAttr "Flame_AdultSG.msg" "materialInfo1.sg";
connectAttr "A_Fire.msg" "materialInfo1.m";
connectAttr "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.msg" "materialInfo1.t" 
		-na;
connectAttr "place2dTexture1.o" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.uv"
		;
connectAttr "place2dTexture1.ofu" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ofu"
		;
connectAttr "place2dTexture1.ofv" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ofv"
		;
connectAttr "place2dTexture1.rf" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.rf"
		;
connectAttr "place2dTexture1.reu" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.reu"
		;
connectAttr "place2dTexture1.rev" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.rev"
		;
connectAttr "place2dTexture1.vt1" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt1"
		;
connectAttr "place2dTexture1.vt2" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt2"
		;
connectAttr "place2dTexture1.vt3" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt3"
		;
connectAttr "place2dTexture1.vc1" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vc1"
		;
connectAttr "place2dTexture1.ofs" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.fs"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cme"
		;
connectAttr ":defaultColorMgtGlobals.cfe" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cmcf"
		;
connectAttr ":defaultColorMgtGlobals.cfp" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cmcp"
		;
connectAttr ":defaultColorMgtGlobals.wsn" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ws"
		;
connectAttr "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.oc" "A_Fire1.c";
connectAttr "A_Fire1.oc" "Flame_AdultSG1.ss";
connectAttr "Flame_AdultSG1.msg" "materialInfo2.sg";
connectAttr "A_Fire1.msg" "materialInfo2.m";
connectAttr "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.msg" "materialInfo2.t" 
		-na;
connectAttr "place2dTexture2.o" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.uv"
		;
connectAttr "place2dTexture2.ofu" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ofu"
		;
connectAttr "place2dTexture2.ofv" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ofv"
		;
connectAttr "place2dTexture2.rf" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.rf"
		;
connectAttr "place2dTexture2.reu" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.reu"
		;
connectAttr "place2dTexture2.rev" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.rev"
		;
connectAttr "place2dTexture2.vt1" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt1"
		;
connectAttr "place2dTexture2.vt2" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt2"
		;
connectAttr "place2dTexture2.vt3" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt3"
		;
connectAttr "place2dTexture2.vc1" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vc1"
		;
connectAttr "place2dTexture2.ofs" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.fs"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cme"
		;
connectAttr ":defaultColorMgtGlobals.cfe" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cmcf"
		;
connectAttr ":defaultColorMgtGlobals.cfp" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cmcp"
		;
connectAttr ":defaultColorMgtGlobals.wsn" "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ws"
		;
connectAttr "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.oc" "_Fire_Adult_BLENDSHADES:A_Fire.c"
		;
connectAttr "_Fire_Adult_BLENDSHADES:A_Fire.oc" "_Fire_Adult_BLENDSHADES:Flame_AdultSG.ss"
		;
connectAttr "_Fire_Adult_BLENDSHADES:Flame_AdultSG.msg" "_Fire_Adult_BLENDSHADES:materialInfo1.sg"
		;
connectAttr "_Fire_Adult_BLENDSHADES:A_Fire.msg" "_Fire_Adult_BLENDSHADES:materialInfo1.m"
		;
connectAttr "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.msg" "_Fire_Adult_BLENDSHADES:materialInfo1.t"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.o" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.uv"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.ofu" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ofu"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.ofv" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ofv"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.rf" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.rf"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.reu" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.reu"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.rev" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.rev"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.vt1" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt1"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.vt2" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt2"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.vt3" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt3"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.vc1" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vc1"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.ofs" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.fs"
		;
connectAttr ":defaultColorMgtGlobals.cme" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cme"
		;
connectAttr ":defaultColorMgtGlobals.cfe" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cmcf"
		;
connectAttr ":defaultColorMgtGlobals.cfp" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cmcp"
		;
connectAttr ":defaultColorMgtGlobals.wsn" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ws"
		;
connectAttr "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.oc" "_Fire_Adult_BLENDSHADES:A_Fire1.c"
		;
connectAttr "_Fire_Adult_BLENDSHADES:A_Fire1.oc" "_Fire_Adult_BLENDSHADES:Flame_AdultSG1.ss"
		;
connectAttr "_Fire_Adult_BLENDSHADES:Flame_AdultSG1.msg" "_Fire_Adult_BLENDSHADES:materialInfo2.sg"
		;
connectAttr "_Fire_Adult_BLENDSHADES:A_Fire1.msg" "_Fire_Adult_BLENDSHADES:materialInfo2.m"
		;
connectAttr "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.msg" "_Fire_Adult_BLENDSHADES:materialInfo2.t"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.o" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.uv"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.ofu" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ofu"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.ofv" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ofv"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.rf" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.rf"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.reu" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.reu"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.rev" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.rev"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.vt1" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt1"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.vt2" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt2"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.vt3" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt3"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.vc1" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vc1"
		;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.ofs" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.fs"
		;
connectAttr ":defaultColorMgtGlobals.cme" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cme"
		;
connectAttr ":defaultColorMgtGlobals.cfe" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cmcf"
		;
connectAttr ":defaultColorMgtGlobals.cfp" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cmcp"
		;
connectAttr ":defaultColorMgtGlobals.wsn" "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ws"
		;
connectAttr "layerManager.dli[1]" "GEOMETRY.id";
connectAttr "layerManager.dli[2]" "JOINTS_REF.id";
connectAttr "layerManager.dli[3]" "JOINTS.id";
connectAttr "layerManager.dli[4]" "CONTROLLERS.id";
connectAttr "ctrl_L_F_Ankle_IK_Multiply_Compensate.oy" "ctrl_L_F_Ankle_IK_conditionBalance_RF.ft"
		;
connectAttr "ctrl_L_F_Ankle_IK_Multiply_Compensate.oy" "ctrl_L_F_Ankle_IK_conditionBalance_RF.ctr"
		;
connectAttr "ctrl_L_F_Ankle_IK_Multiply_Compensate.oy" "ctrl_L_F_Ankle_IK_conditionBalance_RF.cfg"
		;
connectAttr "ctrl_L_F_Ankle_IK_Multiply_Compensate.ox" "ctrl_L_F_Ankle_IK_conditionRoll_RF.ft"
		;
connectAttr "ctrl_L_F_Ankle_IK_Multiply_Compensate.ox" "ctrl_L_F_Ankle_IK_conditionRoll_RF.ctr"
		;
connectAttr "ctrl_L_F_Ankle_IK_Multiply_Compensate.ox" "ctrl_L_F_Ankle_IK_conditionRoll_RF.cfg"
		;
connectAttr "ctrl_L_F_Ankle_IK_conditionBalance_RF.ocr" "ctrl_L_F_Ankle_IK_Multiply_Reverse.i1x"
		;
connectAttr "ctrl_L_F_Ankle_IK_conditionBalance_RF.ocg" "ctrl_L_F_Ankle_IK_Multiply_Reverse.i1y"
		;
connectAttr "ctrl_L_F_Ankle_IK_conditionRoll_RF.ocg" "ctrl_L_F_Ankle_IK_bc_Weight.c1r"
		;
connectAttr "ctrl_L_F_Ankle_IK_conditionRoll_RF.ocg" "ctrl_L_F_Ankle_IK_bc_Weight.c2g"
		;
connectAttr "ctrl_L_F_Ankle_IK_conditionStretch.ocr" "L_F_UpperLeg_JNT_bcTwist.c1r"
		;
connectAttr "L_F_UpperLeg_JNT_bcTwist.opr" "L_F_UpperLeg_JNT_Clamp_Twist.ipr";
connectAttr "L_F_UpperLeg_JNT_MultiplyDivide_Stretch.ox" "ctrl_L_F_Ankle_IK_conditionStretch.ctr"
		;
connectAttr "ctrl_L_B_Ankle_IK_Multiply_Compensate.oy" "ctrl_L_B_Ankle_IK_conditionBalance_RF.ft"
		;
connectAttr "ctrl_L_B_Ankle_IK_Multiply_Compensate.oy" "ctrl_L_B_Ankle_IK_conditionBalance_RF.ctr"
		;
connectAttr "ctrl_L_B_Ankle_IK_Multiply_Compensate.oy" "ctrl_L_B_Ankle_IK_conditionBalance_RF.cfg"
		;
connectAttr "ctrl_L_B_Ankle_IK_Multiply_Compensate.ox" "ctrl_L_B_Ankle_IK_conditionRoll_RF.ft"
		;
connectAttr "ctrl_L_B_Ankle_IK_Multiply_Compensate.ox" "ctrl_L_B_Ankle_IK_conditionRoll_RF.ctr"
		;
connectAttr "ctrl_L_B_Ankle_IK_Multiply_Compensate.ox" "ctrl_L_B_Ankle_IK_conditionRoll_RF.cfg"
		;
connectAttr "ctrl_L_B_Ankle_IK_conditionBalance_RF.ocr" "ctrl_L_B_Ankle_IK_Multiply_Reverse.i1x"
		;
connectAttr "ctrl_L_B_Ankle_IK_conditionBalance_RF.ocg" "ctrl_L_B_Ankle_IK_Multiply_Reverse.i1y"
		;
connectAttr "ctrl_L_B_Ankle_IK_conditionRoll_RF.ocg" "ctrl_L_B_Ankle_IK_bc_Weight.c1r"
		;
connectAttr "ctrl_L_B_Ankle_IK_conditionRoll_RF.ocg" "ctrl_L_B_Ankle_IK_bc_Weight.c2g"
		;
connectAttr "ctrl_L_B_Ankle_IK_conditionStretch.ocr" "L_B_UpperLeg_JNT_bcTwist.c1r"
		;
connectAttr "L_B_UpperLeg_JNT_bcTwist.opr" "L_B_UpperLeg_JNT_Clamp_Twist.ipr";
connectAttr "L_B_UpperLeg_JNT_MultiplyDivide_Stretch.ox" "ctrl_L_B_Ankle_IK_conditionStretch.ctr"
		;
connectAttr "layerManager.dli[5]" "HELPERS.id";
connectAttr "ctrl_R_F_Ankle_IK_Multiply_Compensate.oy" "ctrl_R_F_Ankle_IK_conditionBalance_RF.ft"
		;
connectAttr "ctrl_R_F_Ankle_IK_Multiply_Compensate.oy" "ctrl_R_F_Ankle_IK_conditionBalance_RF.ctr"
		;
connectAttr "ctrl_R_F_Ankle_IK_Multiply_Compensate.oy" "ctrl_R_F_Ankle_IK_conditionBalance_RF.cfg"
		;
connectAttr "ctrl_R_F_Ankle_IK_Multiply_Compensate.ox" "ctrl_R_F_Ankle_IK_conditionRoll_RF.ft"
		;
connectAttr "ctrl_R_F_Ankle_IK_Multiply_Compensate.ox" "ctrl_R_F_Ankle_IK_conditionRoll_RF.ctr"
		;
connectAttr "ctrl_R_F_Ankle_IK_Multiply_Compensate.ox" "ctrl_R_F_Ankle_IK_conditionRoll_RF.cfg"
		;
connectAttr "ctrl_R_F_Ankle_IK_conditionBalance_RF.ocr" "ctrl_R_F_Ankle_IK_Multiply_Reverse.i1x"
		;
connectAttr "ctrl_R_F_Ankle_IK_conditionBalance_RF.ocg" "ctrl_R_F_Ankle_IK_Multiply_Reverse.i1y"
		;
connectAttr "ctrl_R_F_Ankle_IK_conditionRoll_RF.ocg" "ctrl_R_F_Ankle_IK_bc_Weight.c1r"
		;
connectAttr "ctrl_R_F_Ankle_IK_conditionRoll_RF.ocg" "ctrl_R_F_Ankle_IK_bc_Weight.c2g"
		;
connectAttr "ctrl_R_F_Ankle_IK_conditionStretch.ocr" "R_F_UpperLeg_JNT_bcTwist.c1r"
		;
connectAttr "R_F_UpperLeg_JNT_bcTwist.opr" "R_F_UpperLeg_JNT_Clamp_Twist.ipr";
connectAttr "R_F_UpperLeg_JNT_MultiplyDivide_Stretch.ox" "ctrl_R_F_Ankle_IK_conditionStretch.ctr"
		;
connectAttr "ctrl_R_B_Ankle_IK_Multiply_Compensate.oy" "ctrl_R_B_Ankle_IK_conditionBalance_RF.ft"
		;
connectAttr "ctrl_R_B_Ankle_IK_Multiply_Compensate.oy" "ctrl_R_B_Ankle_IK_conditionBalance_RF.ctr"
		;
connectAttr "ctrl_R_B_Ankle_IK_Multiply_Compensate.oy" "ctrl_R_B_Ankle_IK_conditionBalance_RF.cfg"
		;
connectAttr "ctrl_R_B_Ankle_IK_Multiply_Compensate.ox" "ctrl_R_B_Ankle_IK_conditionRoll_RF.ft"
		;
connectAttr "ctrl_R_B_Ankle_IK_Multiply_Compensate.ox" "ctrl_R_B_Ankle_IK_conditionRoll_RF.ctr"
		;
connectAttr "ctrl_R_B_Ankle_IK_Multiply_Compensate.ox" "ctrl_R_B_Ankle_IK_conditionRoll_RF.cfg"
		;
connectAttr "ctrl_R_B_Ankle_IK_conditionBalance_RF.ocr" "ctrl_R_B_Ankle_IK_Multiply_Reverse.i1x"
		;
connectAttr "ctrl_R_B_Ankle_IK_conditionBalance_RF.ocg" "ctrl_R_B_Ankle_IK_Multiply_Reverse.i1y"
		;
connectAttr "ctrl_R_B_Ankle_IK_conditionRoll_RF.ocg" "ctrl_R_B_Ankle_IK_bc_Weight.c1r"
		;
connectAttr "ctrl_R_B_Ankle_IK_conditionRoll_RF.ocg" "ctrl_R_B_Ankle_IK_bc_Weight.c2g"
		;
connectAttr "ctrl_R_B_Ankle_IK_conditionStretch.ocr" "R_B_UpperLeg_JNT_bcTwist.c1r"
		;
connectAttr "R_B_UpperLeg_JNT_bcTwist.opr" "R_B_UpperLeg_JNT_Clamp_Twist.ipr";
connectAttr "R_B_UpperLeg_JNT_MultiplyDivide_Stretch.ox" "ctrl_R_B_Ankle_IK_conditionStretch.ctr"
		;
connectAttr "L_F_UpperLeg_JNT_Clamp_Twist.opr" "multiplyDivide1.i2x";
connectAttr "L_B_UpperLeg_JNT_Clamp_Twist.opr" "multiplyDivide2.i2x";
connectAttr "R_F_UpperLeg_JNT_Clamp_Twist.opr" "multiplyDivide3.i2x";
connectAttr "R_B_UpperLeg_JNT_Clamp_Twist.opr" "multiplyDivide4.i2x";
connectAttr "_MultiplyDivide_RibbonStretch.ox" "_bcRibbon.c1r";
connectAttr "_bcRibbon.opr" "_ClampRibbon.ipr";
connectAttr "_ClampRibbon.opr" "_MultiplyDivide_RibbonStretch2.i2x";
connectAttr "NeckRibbon__MultiplyDivide_RibbonStretch.ox" "NeckRibbon__bcRibbon.c1r"
		;
connectAttr "NeckRibbon__bcRibbon.opr" "NeckRibbon__ClampRibbon.ipr";
connectAttr "NeckRibbon__ClampRibbon.opr" "NeckRibbon__MultiplyDivide_RibbonStretch2.i2x"
		;
connectAttr "multiplyDivide1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn";
connectAttr "L_F_UpperLeg_JNT_MultiplyDivide_Stretch.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn"
		;
connectAttr "ctrl_L_F_Ankle_IK_conditionStretch.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "L_F_UpperLeg_JNT_bcTwist.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn"
		;
connectAttr "L_F_UpperLeg_JNT_Clamp_Twist.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[17].dn"
		;
connectAttr "L_B_UpperLeg_JNT_MultiplyDivide_Stretch.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[4].dn"
		;
connectAttr "ctrl_L_B_Ankle_IK_conditionStretch.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[6].dn"
		;
connectAttr "L_B_UpperLeg_JNT_bcTwist.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[8].dn"
		;
connectAttr "multiplyDivide2.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[9].dn";
connectAttr "L_B_UpperLeg_JNT_Clamp_Twist.msg" "MayaNodeEditorSavedTabsInfo.tgi[1].ni[11].dn"
		;
connectAttr "R_F_UpperLeg_JNT_MultiplyDivide_Stretch.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[0].dn"
		;
connectAttr "R_F_UpperLeg_JNT_bcTwist.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[3].dn"
		;
connectAttr "ctrl_R_F_Ankle_IK_conditionStretch.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[4].dn"
		;
connectAttr "multiplyDivide3.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[9].dn";
connectAttr "R_F_UpperLeg_JNT_Clamp_Twist.msg" "MayaNodeEditorSavedTabsInfo.tgi[2].ni[16].dn"
		;
connectAttr "R_B_UpperLeg_JNT_bcTwist.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[4].dn"
		;
connectAttr "R_B_UpperLeg_JNT_Clamp_Twist.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[8].dn"
		;
connectAttr "ctrl_R_B_Ankle_IK_conditionStretch.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[9].dn"
		;
connectAttr "R_B_UpperLeg_JNT_MultiplyDivide_Stretch.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[12].dn"
		;
connectAttr "multiplyDivide4.msg" "MayaNodeEditorSavedTabsInfo.tgi[3].ni[14].dn"
		;
connectAttr "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.oc" "_Fire_Adult_LEFT_LEGS___Copy_A_Fire.c"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_A_Fire.oc" "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG.ss"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG.msg" "_Fire_Adult_LEFT_LEGS___Copy_materialInfo1.sg"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_A_Fire.msg" "_Fire_Adult_LEFT_LEGS___Copy_materialInfo1.m"
		;
connectAttr "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.msg" "_Fire_Adult_LEFT_LEGS___Copy_materialInfo1.t"
		 -na;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.o" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.uv"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.ofu" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.ofu"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.ofv" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.ofv"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.rf" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.rf"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.reu" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.reu"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.rev" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.rev"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.vt1" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.vt1"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.vt2" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.vt2"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.vt3" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.vt3"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.vc1" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.vc1"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.ofs" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.fs"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.cme"
		;
connectAttr ":defaultColorMgtGlobals.cfe" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.cmcf"
		;
connectAttr ":defaultColorMgtGlobals.cfp" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.cmcp"
		;
connectAttr ":defaultColorMgtGlobals.wsn" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.ws"
		;
connectAttr "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.oc" "_Fire_Adult_LEFT_LEGS___Copy_A_Fire1.c"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_A_Fire1.oc" "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG1.ss"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG1.msg" "_Fire_Adult_LEFT_LEGS___Copy_materialInfo2.sg"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_A_Fire1.msg" "_Fire_Adult_LEFT_LEGS___Copy_materialInfo2.m"
		;
connectAttr "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.msg" "_Fire_Adult_LEFT_LEGS___Copy_materialInfo2.t"
		 -na;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.o" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.uv"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.ofu" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.ofu"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.ofv" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.ofv"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.rf" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.rf"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.reu" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.reu"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.rev" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.rev"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.vt1" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.vt1"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.vt2" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.vt2"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.vt3" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.vt3"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.vc1" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.vc1"
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.ofs" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.fs"
		;
connectAttr ":defaultColorMgtGlobals.cme" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.cme"
		;
connectAttr ":defaultColorMgtGlobals.cfe" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.cmcf"
		;
connectAttr ":defaultColorMgtGlobals.cfp" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.cmcp"
		;
connectAttr ":defaultColorMgtGlobals.wsn" "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.ws"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.oc" "_Fire_Adult_BLENDSHADES1:A_Fire.c"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:A_Fire.oc" "_Fire_Adult_BLENDSHADES1:Flame_AdultSG.ss"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:Flame_AdultSG.msg" "_Fire_Adult_BLENDSHADES1:materialInfo1.sg"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:A_Fire.msg" "_Fire_Adult_BLENDSHADES1:materialInfo1.m"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.msg" "_Fire_Adult_BLENDSHADES1:materialInfo1.t"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.o" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.uv"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.ofu" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ofu"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.ofv" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ofv"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.rf" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.rf"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.reu" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.reu"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.rev" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.rev"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.vt1" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt1"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.vt2" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt2"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.vt3" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vt3"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.vc1" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.vc1"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.ofs" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.fs"
		;
connectAttr ":defaultColorMgtGlobals.cme" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cme"
		;
connectAttr ":defaultColorMgtGlobals.cfe" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cmcf"
		;
connectAttr ":defaultColorMgtGlobals.cfp" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.cmcp"
		;
connectAttr ":defaultColorMgtGlobals.wsn" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.ws"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.oc" "_Fire_Adult_BLENDSHADES1:A_Fire1.c"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:A_Fire1.oc" "_Fire_Adult_BLENDSHADES1:Flame_AdultSG1.ss"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:Flame_AdultSG1.msg" "_Fire_Adult_BLENDSHADES1:materialInfo2.sg"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:A_Fire1.msg" "_Fire_Adult_BLENDSHADES1:materialInfo2.m"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.msg" "_Fire_Adult_BLENDSHADES1:materialInfo2.t"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.o" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.uv"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.ofu" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ofu"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.ofv" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ofv"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.rf" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.rf"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.reu" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.reu"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.rev" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.rev"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.vt1" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt1"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.vt2" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt2"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.vt3" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vt3"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.vc1" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.vc1"
		;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.ofs" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.fs"
		;
connectAttr ":defaultColorMgtGlobals.cme" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cme"
		;
connectAttr ":defaultColorMgtGlobals.cfe" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cmcf"
		;
connectAttr ":defaultColorMgtGlobals.cfp" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.cmcp"
		;
connectAttr ":defaultColorMgtGlobals.wsn" "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.ws"
		;
connectAttr "MapFBXASC032FBXASC0352.oc" "Knight_A_ncl1_1.c";
connectAttr "Knight_A_ncl1_1.oc" "L_Eye_OpenSG.ss";
connectAttr "L_Eye_OpenSG.msg" "materialInfo3.sg";
connectAttr "Knight_A_ncl1_1.msg" "materialInfo3.m";
connectAttr "MapFBXASC032FBXASC0352.msg" "materialInfo3.t" -na;
connectAttr ":defaultColorMgtGlobals.cme" "MapFBXASC032FBXASC0352.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "MapFBXASC032FBXASC0352.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "MapFBXASC032FBXASC0352.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "MapFBXASC032FBXASC0352.ws";
connectAttr "place2dTexture3.o" "MapFBXASC032FBXASC0352.uv";
connectAttr "place2dTexture3.ofu" "MapFBXASC032FBXASC0352.ofu";
connectAttr "place2dTexture3.ofv" "MapFBXASC032FBXASC0352.ofv";
connectAttr "place2dTexture3.rf" "MapFBXASC032FBXASC0352.rf";
connectAttr "place2dTexture3.reu" "MapFBXASC032FBXASC0352.reu";
connectAttr "place2dTexture3.rev" "MapFBXASC032FBXASC0352.rev";
connectAttr "place2dTexture3.vt1" "MapFBXASC032FBXASC0352.vt1";
connectAttr "place2dTexture3.vt2" "MapFBXASC032FBXASC0352.vt2";
connectAttr "place2dTexture3.vt3" "MapFBXASC032FBXASC0352.vt3";
connectAttr "place2dTexture3.vc1" "MapFBXASC032FBXASC0352.vc1";
connectAttr "place2dTexture3.ofs" "MapFBXASC032FBXASC0352.fs";
connectAttr "MapFBXASC032FBXASC0353.oc" "Knight_A_ncl1_2.c";
connectAttr "Knight_A_ncl1_2.oc" "L_Eye_OpenSG1.ss";
connectAttr "L_Eye_OpenSG1.msg" "materialInfo4.sg";
connectAttr "Knight_A_ncl1_2.msg" "materialInfo4.m";
connectAttr "MapFBXASC032FBXASC0353.msg" "materialInfo4.t" -na;
connectAttr ":defaultColorMgtGlobals.cme" "MapFBXASC032FBXASC0353.cme";
connectAttr ":defaultColorMgtGlobals.cfe" "MapFBXASC032FBXASC0353.cmcf";
connectAttr ":defaultColorMgtGlobals.cfp" "MapFBXASC032FBXASC0353.cmcp";
connectAttr ":defaultColorMgtGlobals.wsn" "MapFBXASC032FBXASC0353.ws";
connectAttr "place2dTexture4.o" "MapFBXASC032FBXASC0353.uv";
connectAttr "place2dTexture4.ofu" "MapFBXASC032FBXASC0353.ofu";
connectAttr "place2dTexture4.ofv" "MapFBXASC032FBXASC0353.ofv";
connectAttr "place2dTexture4.rf" "MapFBXASC032FBXASC0353.rf";
connectAttr "place2dTexture4.reu" "MapFBXASC032FBXASC0353.reu";
connectAttr "place2dTexture4.rev" "MapFBXASC032FBXASC0353.rev";
connectAttr "place2dTexture4.vt1" "MapFBXASC032FBXASC0353.vt1";
connectAttr "place2dTexture4.vt2" "MapFBXASC032FBXASC0353.vt2";
connectAttr "place2dTexture4.vt3" "MapFBXASC032FBXASC0353.vt3";
connectAttr "place2dTexture4.vc1" "MapFBXASC032FBXASC0353.vc1";
connectAttr "place2dTexture4.ofs" "MapFBXASC032FBXASC0353.fs";
connectAttr "Flame_AdultSG.pa" ":renderPartition.st" -na;
connectAttr "Flame_AdultSG1.pa" ":renderPartition.st" -na;
connectAttr "_Fire_Adult_BLENDSHADES:Flame_AdultSG.pa" ":renderPartition.st" -na
		;
connectAttr "_Fire_Adult_BLENDSHADES:Flame_AdultSG1.pa" ":renderPartition.st" -na
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG.pa" ":renderPartition.st"
		 -na;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_Flame_AdultSG1.pa" ":renderPartition.st"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES1:Flame_AdultSG.pa" ":renderPartition.st" -na
		;
connectAttr "_Fire_Adult_BLENDSHADES1:Flame_AdultSG1.pa" ":renderPartition.st" -na
		;
connectAttr "L_Eye_OpenSG.pa" ":renderPartition.st" -na;
connectAttr "L_Eye_OpenSG1.pa" ":renderPartition.st" -na;
connectAttr "A_Fire.msg" ":defaultShaderList1.s" -na;
connectAttr "A_Fire1.msg" ":defaultShaderList1.s" -na;
connectAttr "_Fire_Adult_BLENDSHADES:A_Fire.msg" ":defaultShaderList1.s" -na;
connectAttr "_Fire_Adult_BLENDSHADES:A_Fire1.msg" ":defaultShaderList1.s" -na;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_A_Fire.msg" ":defaultShaderList1.s" -na
		;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_A_Fire1.msg" ":defaultShaderList1.s" -na
		;
connectAttr "_Fire_Adult_BLENDSHADES1:A_Fire.msg" ":defaultShaderList1.s" -na;
connectAttr "_Fire_Adult_BLENDSHADES1:A_Fire1.msg" ":defaultShaderList1.s" -na;
connectAttr "Knight_A_ncl1_1.msg" ":defaultShaderList1.s" -na;
connectAttr "Knight_A_ncl1_2.msg" ":defaultShaderList1.s" -na;
connectAttr "place2dTexture1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place2dTexture2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture1.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES:place2dTexture2.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_F_Ankle_IK_conditionBalance_RF.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_F_Ankle_IK_conditionRoll_RF.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_F_Ankle_IK_Multiply_Compensate.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_F_Ankle_IK_Multiply_Reverse.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_F_Ankle_IK_bc_Weight.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "L_F_UpperLeg_JNT_MultiplyDivide_Stretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "L_F_UpperLeg_JNT_bcTwist.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "L_F_UpperLeg_JNT_Clamp_Twist.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "ctrl_L_F_Ankle_IK_conditionStretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_B_Ankle_IK_conditionBalance_RF.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_B_Ankle_IK_conditionRoll_RF.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_B_Ankle_IK_Multiply_Compensate.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_B_Ankle_IK_Multiply_Reverse.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_L_B_Ankle_IK_bc_Weight.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "L_B_UpperLeg_JNT_MultiplyDivide_Stretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "L_B_UpperLeg_JNT_bcTwist.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "L_B_UpperLeg_JNT_Clamp_Twist.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "ctrl_L_B_Ankle_IK_conditionStretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_F_Ankle_IK_conditionBalance_RF.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_F_Ankle_IK_conditionRoll_RF.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_F_Ankle_IK_Multiply_Compensate.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_F_Ankle_IK_Multiply_Reverse.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_F_Ankle_IK_bc_Weight.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "R_F_UpperLeg_JNT_MultiplyDivide_Stretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "R_F_UpperLeg_JNT_bcTwist.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "R_F_UpperLeg_JNT_Clamp_Twist.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "ctrl_R_F_Ankle_IK_conditionStretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_B_Ankle_IK_conditionBalance_RF.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_B_Ankle_IK_conditionRoll_RF.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_B_Ankle_IK_Multiply_Compensate.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_B_Ankle_IK_Multiply_Reverse.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "ctrl_R_B_Ankle_IK_bc_Weight.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "R_B_UpperLeg_JNT_MultiplyDivide_Stretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "R_B_UpperLeg_JNT_bcTwist.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "R_B_UpperLeg_JNT_Clamp_Twist.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "ctrl_R_B_Ankle_IK_conditionStretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "multiplyDivide1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multiplyDivide2.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multiplyDivide3.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multiplyDivide4.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "_MultiplyDivide_RibbonStretch.msg" ":defaultRenderUtilityList1.u" -na
		;
connectAttr "_bcRibbon.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "_ClampRibbon.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "_MultiplyDivide_RibbonStretch2.msg" ":defaultRenderUtilityList1.u" 
		-na;
connectAttr "NeckRibbon__MultiplyDivide_RibbonStretch.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "NeckRibbon__bcRibbon.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "NeckRibbon__ClampRibbon.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "NeckRibbon__MultiplyDivide_RibbonStretch2.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture1.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "_Fire_Adult_LEFT_LEGS___Copy_place2dTexture2.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture1.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES1:place2dTexture2.msg" ":defaultRenderUtilityList1.u"
		 -na;
connectAttr "place2dTexture3.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "place2dTexture4.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.msg" ":defaultTextureList1.tx"
		 -na;
connectAttr "Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.msg" ":defaultTextureList1.tx"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.msg" ":defaultTextureList1.tx"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.msg" ":defaultTextureList1.tx"
		 -na;
connectAttr "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353037.msg" ":defaultTextureList1.tx"
		 -na;
connectAttr "Fire_3:Fire_1__2_:MapFBXASC032FBXASC0353038.msg" ":defaultTextureList1.tx"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353037.msg" ":defaultTextureList1.tx"
		 -na;
connectAttr "_Fire_Adult_BLENDSHADES1:Fire_2:Fire_1__2_:MapFBXASC032FBXASC0353038.msg" ":defaultTextureList1.tx"
		 -na;
connectAttr "MapFBXASC032FBXASC0352.msg" ":defaultTextureList1.tx" -na;
connectAttr "MapFBXASC032FBXASC0353.msg" ":defaultTextureList1.tx" -na;
// End of Arxiu 001 - Base.ma
