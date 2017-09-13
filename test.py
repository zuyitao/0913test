from com.jiyun import animal;
dog=animal.Dog("黑色","肉","50kg")
cat=animal.Cat("白色","鱼","20kg")
num=animal.Animal.ani_count

print("狗：")
dog.setzuoyong("看门")
dog.ani_mothed()
print("猫：")
cat.setname("咪咪")
cat.ani_mothed()

print("动物数量：",num)