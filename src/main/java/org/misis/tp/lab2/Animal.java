package org.misis.tp.lab2;

public abstract class Animal implements Pet {
    private final String name;
    private int age;

    public Animal(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public void happyBirthday() {
        age++;
    }

    public abstract void express();
    public abstract int getAgeInHumanYears();

    @Override
    public String getName() { return name; }

    @Override
    public int getAge() { return age; }
}